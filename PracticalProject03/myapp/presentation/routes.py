"""
Module: __routes__.py

Docstring for __routes__.py of Practical Project 3

Course: CST8002 Section 010 Programming Language Research Project
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: 
    This module represents Flask framework, loading data from appointed data file. 

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

"""
from flask import render_template, request, redirect, url_for
from myapp import app
from myapp.business.record_memory_storage import RecordStorage
from myapp.model.shorebird_monitoring_record import ShorebirdMonitoringRecord

storage = RecordStorage()
filename = "pacific_rim_npr_coastalmarine_migratory_shorebird_habitat_use_2011-2017_data.csv"
storage.load_from_data(filename, 100)

@app.route('/')
def index():
    records = storage.get_records()
    return render_template('index.html', records=records)

@app.route('/create', methods=['GET', 'POST'])
def create():
    """
    Route handler for creating a new record.

    GET:  Displays the create form.
    POST: Reads form input, creates a new ShorebirdMonitoringRecord
          object, adds it to storage, and redirects to home page.

    Returns:
        GET:  Rendered create.html template.
        POST: Redirect to index page.
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
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    """
    Route handler for editing an existing record by index.

    GET:  Displays the edit form pre-filled with current record values.
    POST: Reads form input, updates the record in storage,
          and redirects to home page.

    Parameters:
        index (int): Position of the record in the storage list.

    Returns:
        GET:  Rendered edit.html template with current record values.
        POST: Redirect to index page.
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
        return redirect(url_for('index'))
    return render_template('edit.html', record=record, index=index)