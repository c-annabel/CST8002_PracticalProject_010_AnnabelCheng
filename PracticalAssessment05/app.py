"""
Course: CST8002 Section 010 Programming Language Research Project
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description:
    Proof-of-concept standalone Flask search application.
    Reads 2025 SUV records from a CSV file and allows the user
    to search by make/model text and filter by review stars.

References:
    [1] Wong A. (Aug. 2, 2020). How to build a simple search engine
        using Flask. Medium. [Online]. Available at:
        https://medium.com/analytics-vidhya/how-to-build-a-simple-search-engine-using-flask-4f3c01fe80fa
        [Accessed: Apr. 1, 2026].
    [2] Pallets. (2010). Welcome to Flask - Flask documentation (3.1.x).
        Flask Official Documentation. [Online]. Available at:
        https://flask.palletsprojects.com/en/stable/
        [Accessed: Mar. 11, 2026].

Version: 
        Python 3.14.3
        pip 26.0.1
        Flask 3.1.3
        
Due Date: 2026.04.4

"""

import csv
import os
from flask import Flask, render_template, request
 
app = Flask(__name__)
 
DATA_FILE = os.path.join(os.path.dirname(__file__), "suvs.csv")
 
 
def load_suvs():
    """
    Reads all SUV records from the CSV data file.
 
    Each row contains make, model, and stars columns.
    The stars value is converted to an integer on load.
 
    Returns:
        list[dict]: A list of SUV record dictionaries.
    """
    records = []
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append({
                "make":  row["make"].strip(),
                "model": row["model"].strip(),
                "stars": int(row["stars"].strip())
            })
    return records
 
 
def filter_suvs(suvs, query, rating):
    """
    Filters a list of SUV records by text query and star rating.
 
    Both filters are always applied together. The text query performs
    a case-insensitive partial match against both make and model fields.
    The star filter keeps only records with stars = rating.
 
    Args:
        suvs      (list[dict]): Full list of SUV records.
        query     (str):        Text to search in make and model.
        rating (int):        Star rating (0 = no filter).
 
    Returns:
        list[dict]: Filtered list of SUV records.
 
    References:
        [1] Wong A. (Aug. 2, 2020). How to build a simple search engine
            using Flask. Medium.
    """
    results = suvs
 
    if query:
        q = query.lower()
        results = [
            r for r in results
            if q in r["make"].lower() or q in r["model"].lower()
        ]
 
    if rating > 0:
        results = [r for r in results if r["stars"] == rating]
 
    return results
 
 
@app.route("/")
def search():
    """
    Home route. Single page that handles both display and search/filter.
 
    Reads optional GET parameters 'query' and 'rating' from the
    request. When no parameters are present all records are shown.
    Both filters are always applied at the same time.
 
    Returns:
        Rendered search.html template with filtered results and form state.
    """
    query     = request.args.get("query",     "").strip()
    rating = request.args.get("rating", "0")
    rating = int(rating) if rating.isdigit() else 0
 
    suvs    = load_suvs()
    results = filter_suvs(suvs, query, rating)
 
    return render_template(
        "search.html",
        results=results,
        query=query,
        rating=rating,
        total=len(results)
    )
 
 
if __name__ == "__main__":
    app.run(debug=True)
 