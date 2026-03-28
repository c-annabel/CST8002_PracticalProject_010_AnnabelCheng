"""
Module: __init__.py

Docstring for __init__.py of Practical Project 3

Course: CST8002 Section 010 Programming Language Research Project
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: 
    This module initializes the Flask application instance for the
    Shorebird Monitoring Records MVC web application.

    It configures the template folder path to point to the
    presentation layer's templates directory, sets the secret key
    required for flash messaging, and registers the routes module
    from the presentation layer.

Architecture:
    This is the application entry point for the Flask MVC structure:
        __init__.py (app setup) → presentation/routes.py (Controller)
                                → presentation/templates/ (Views)
                                → business/ (Business Layer)
                                → persistence/ (Persistence Layer)
                                → model/ (Model Layer)

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
[4] Anthropic. (2026). DocString Assistance. Claude (claude-sonnet-4-6) [Large language model]. [Online].
    Available at: https://claude.ai
    [Accessed: Mar. 27, 2026].

"""

from flask import Flask
import os

"""
Constant: app (Flask)
Purpose:  The central Flask application instance.
          template_folder is explicitly set to point to
          presentation/templates/ within the myapp package directory.
"""
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'presentation', 'templates'))

"""
Constant: secret_key (str)
Purpose:  Required by Flask to cryptographically sign session cookies,
          enabling the flash() messaging system to work correctly.
"""
app.secret_key = "shorebird_cst8002"

# Register routes from the presentation layer.
# This import must remain at the bottom to avoid circular imports
# between app initialization and route registration.
from myapp.presentation import routes