"""
Module: __routes__.py

Docstring for __routes__.py of Practical Project 3

Course: CST8002 Section 010 Programming Language Research Project
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: 
    This module represents the Controller layer of the Flask MVC
    web application for the Shorebird Monitoring Records project.
 
    It defines all URL route functions that handle HTTP requests,
    delegate data operations to the Business Layer, and return
    rendered HTML templates as responses to the browser.
 
    Routes implemented:
        GET  /                      → index()  : Display all records
        GET  /view/<index>          → view()   : Display one record
        GET  POST /create           → create() : Create a new record
        GET  POST /edit/<index>     → edit()   : Edit an existing record
        GET  POST /delete/<index>   → delete() : Delete a record
        GET  /reload                → reload() : Reload dataset from file
        GET  /save                  → save()   : Save records to UUID CSV file
 
Architecture:
    Follows MVC pattern within N-Layered architecture:
        View (templates/) → Controller (routes.py)
                          → Business (record_memory_storage.py)
                          → Persistence (file_handler.py)
                          → Model (shorebird_monitoring_record.py)

Version: 
        Python 3.14.3
        pip 26.0.1
        Flask 3.1.3
        Werkzeug 3.1.7
Due Date: 2026.03.29

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalProject03

Reference: 
[1] Parks Canada. (Oct. 1, 2017). Migratory Shorebird Habitat Use - Pacific Rim. open.canada.ca. [Online]. 
    Available at: https://open.canada.ca/data/en/dataset/e0aa39b6-67c0-4863-bdad-d74e73870697 
    [Accessed: Feb. 18, 2026].
[2] Pallets. (2010). Welcome to Flask — Flask documentation (3.1.x). Flask Official Documentation. Pallets. [Online].
    Available at: https://flask.palletsprojects.com/en/stable/ 
    [Accessed: Mar. 20, 2026].
[3] GeeksforGeeks. (Mar. 7, 2026). Flask tutorial. GeeksforGeeks. [Online]. 
    Available at: https://www.geeksforgeeks.org/python/flask-tutorial/ 
    [Accessed: Mar. 20, 2026].
[4] Pallets Projects. (2010). Templates — Flask documentation (3.1.x). Flask Official Documentation. Pallets. [Online].
    Available at: https://flask.palletsprojects.com/en/stable/templating/
    [Accessed: Mar. 21, 2026].
[5] Anthropic. (2026). DocString Assistance. Claude (claude-sonnet-4-6) [Large language model]. [Online].
    Available at: https://claude.ai
    [Accessed: Mar. 27, 2026].

"""
from flask import render_template, request, redirect, url_for, flash
from myapp import app
from myapp.business.record_memory_storage import RecordStorage
from myapp.model.shorebird_monitoring_record import ShorebirdMonitoringRecord

# ==============================
# Constants
# ==============================
 
"""
Constant: filename (str)
Purpose:  The dataset CSV filename loaded into memory on application startup.
"""
filename = "pacific_rim_npr_coastalmarine_migratory_shorebird_habitat_use_2011-2017_data.csv"
 
"""
Constant: limit (int)
Purpose:  Maximum number of records to load from the dataset file.
"""
limit = 100
 
# ==============================
# Business Layer Initialization
# ==============================
 
"""
Module-level variable: storage (RecordStorage)
Purpose:  A single shared RecordStorage instance used across all
          route functions for the duration of the application session.
          Records are loaded from the dataset file on startup.
"""
storage = RecordStorage()
storage.load_from_data(filename, limit)
 
 
# ==============================
# Route: View All Records
# URL:   GET /
# ==============================
 
@app.route('/')
def index():
    """
    Route handler for the home page.
 
    Retrieves all records currently held in memory from the
    Business Layer and passes them to the index.html template
    for display in a formatted table.
 
    Returns:
        Response: Rendered index.html template with all records.
    """
    records = storage.get_records()
    return render_template('index.html', records=records)
 
 
# ==============================
# Route: View One Record
# URL:   GET /view/<index>
# ==============================
 
@app.route('/view/<int:index>')
def view(index):
    """
    Route handler for viewing a single record by index.
 
    Retrieves one record from the Business Layer by its index
    position and passes it to the view_one.html template for display.
    Redirects to the home page if the index is invalid.
 
    Parameters:
        index (int): Position of the record in the storage list.
 
    Returns:
        Response: Rendered view_one.html template with the selected record,
                  or redirect to index page if record not found.
    """
    record = storage.get_record_by_index(index)
    if record is None:
        return redirect(url_for('index'))
    return render_template('view_one.html', record=record, index=index)
 
 
# ==============================
# Route: Create Record
# URL:   GET POST /create
# ==============================
 
@app.route('/create', methods=['GET', 'POST'])
def create():
    """
    Route handler for creating a new record.
 
    GET:  Displays the empty create form to the user.
    POST: Reads form input fields, instantiates a new
          ShorebirdMonitoringRecord object, adds it to the
          Business Layer storage, and redirects to the home page
          with a success flash message.
 
    Returns:
        GET:  Rendered create.html template.
        POST: Redirect to index page with success flash message.
    """
    if request.method == 'POST':
        new_record = ShorebirdMonitoringRecord(
            request.form['site'],
            request.form['area'],
            request.form['date'],
            request.form['time'],
            request.form['code'],
            request.form['count']
        )
        storage.add_record(new_record)
        flash("Record created successfully.", "success")
        return redirect(url_for('index'))
    return render_template('create.html')
 
 
# ==============================
# Route: Edit Record
# URL:   GET POST /edit/<index>
# ==============================
 
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    """
    Route handler for editing an existing record by index.
 
    GET:  Retrieves the record from storage and displays the edit
          form pre-filled with the record's current values.
    POST: Reads updated form input fields, delegates the update
          to the Business Layer, and redirects to the home page
          with a success flash message.
          Redirects to the home page if the index is invalid.
 
    Parameters:
        index (int): Position of the record in the storage list.
 
    Returns:
        GET:  Rendered edit.html template with current record values.
        POST: Redirect to index page with success flash message,
              or redirect to index if record not found.
    """
    record = storage.get_record_by_index(index)
    if record is None:
        return redirect(url_for('index'))
 
    if request.method == 'POST':
        storage.edit_record_by_index(
            index,
            site_identification=request.form['site'],
            area=request.form['area'],
            visit_date=request.form['date'],
            start_time=request.form['time'],
            species_code=request.form['code'],
            count=request.form['count']
        )
        flash("Record updated successfully.", "success")
        return redirect(url_for('index'))
    return render_template('edit.html', record=record, index=index)
 
 
# ==============================
# Route: Delete Record
# URL:   GET POST /delete/<index>
# ==============================
 
@app.route('/delete/<int:index>', methods=['GET', 'POST'])
def delete(index):
    """
    Route handler for deleting a record by index.
 
    GET:  Retrieves the record from storage and displays a
          confirmation page showing the selected record's details.
    POST: Deletes the record from the Business Layer storage
          and redirects to the home page with a danger flash message.
          Redirects to the home page if the index is invalid.
 
    Parameters:
        index (int): Position of the record in the storage list.
 
    Returns:
        GET:  Rendered delete.html confirmation template.
        POST: Redirect to index page with danger flash message,
              or redirect to index if record not found.
    """
    record = storage.get_record_by_index(index)
    if record is None:
        return redirect(url_for('index'))
 
    if request.method == 'POST':
        storage.delete_record_by_index(index)
        flash("Record deleted successfully.", "danger")
        return redirect(url_for('index'))
    return render_template('delete.html', record=record, index=index)
 
 
# ==============================
# Route: Reload Dataset
# URL:   GET /reload
# ==============================
 
@app.route('/reload')
def reload():
    """
    Route handler for reloading the dataset from the CSV file.
 
    Replaces all current in-memory records with a fresh load
    from the original dataset file by calling the Business Layer.
    Redirects to the home page with a success flash message
    confirming the number of records reloaded.
 
    Returns:
        Response: Redirect to index page with success flash message.
    """
    storage.load_from_data(filename, limit)
    flash(f"Dataset reloaded successfully. {storage.get_total_loaded()} records loaded.", "success")
    return redirect(url_for('index'))
 
 
# ==============================
# Route: Save to UUID Filename
# URL:   GET /save
# ==============================
 
@app.route('/save')
def save():
    """
    Route handler for saving current in-memory records
    to a new CSV file with a UUID-generated filename.
 
    Delegates the file writing operation to the Business Layer,
    which in turn calls the Persistence Layer to write the file.
    Redirects to the home page with a success flash message
    displaying the newly generated filename.
 
    Returns:
        Response: Redirect to index page with success flash message
                  showing the UUID-generated filename.
    """
    new_file = storage.save_to_new_file()
    flash(f"Data saved successfully to: {new_file}", "success")
    return redirect(url_for('index'))