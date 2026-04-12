# CST8002 Programming Language Research Project
### Algonquin College — Winter 2026

---

## Overview

This repository documents a four-part iterative software development project completed as part of **CST8002 Programming Language Research Project** at Algonquin College. The project explores Python as a programming language through progressively advanced real-world applications, using a shorebird monitoring dataset published by Parks Canada.

Each practical project builds directly on top of the previous one, demonstrating the ability to refactor, extend, and maintain a growing codebase across multiple releases while applying industry-standard software engineering practices.

---

## Dataset

**Migratory Shorebird Habitat Use — Pacific Rim National Park Reserve (2011–2017)**
- Source: Parks Canada / Open Government Canada
- Format: CSV
- Fields: Site Identification, Area, Visit Date, Start Time, Species Code, Count

Parks Canada. (Oct. 1, 2017). Migratory Shorebird Habitat Use - Pacific Rim. open.canada.ca. [Online].  
Available at: https://open.canada.ca/data/en/dataset/e0aa39b6-67c0-4863-bdad-d74e73870697. 
[Accessed: Feb. 18, 2026].

---

## Project Progression

```
Practical Project 1 — Foundation & Language Exploration
        ↓
Practical Project 2 — N-Layered Terminal CRUD Application
        ↓
Practical Project 3 — Flask MVC Web Application
        ↓
Practical Project 4 — Advanced Feature Extension (Search & Filter)
```

---

## Practical Project 1 — Language Research & Foundation

**Branch:** `main` | **Tag:** `V1.0`

### What Was Built
An introductory Python program that established familiarity with the language syntax, data types, control structures, and basic file handling.

### Key Skills Demonstrated
- Python syntax and language fundamentals
- Reading and parsing CSV files using Python's built-in `csv` module
- Basic input/output and console interaction
- GitHub repository setup and version control workflow

---

## Practical Project 2 — N-Layered Terminal CRUD Application

**Branch:** `project2` | **Tag:** `V2.0` `V2.01`

### What Was Built
A fully functional terminal-based CRUD application for managing shorebird monitoring records, structured using a four-layer N-layered architecture.

### Architecture
```
Presentation Layer  →  __main__.py         (console menu & user interaction)
Business Layer      →  record_memory_storage.py  (in-memory data management)
Persistence Layer   →  file_handler.py     (CSV file I/O)
Model Layer         →  shorebird_monitoring_record.py  (entity/DTO class)
```

### Features Implemented
- Load dataset from CSV file into memory on startup
- Display all records in a formatted table
- Display a single record by index
- Display a range of records
- Create a new record
- Edit an existing record
- Delete a record with confirmation
- Save in-memory records to a new CSV file with a UUID-generated filename
- Reload the dataset from the original file at runtime

### Key Skills Demonstrated
- N-Layered software architecture and Separation of Concerns
- Object-Oriented Programming — entity class with getters and setters
- CSV file reading and writing using Python's `csv` module
- UUID generation using Python's `uuid` module
- Input validation and error handling
- Python packaging — organised code into packages using `__init__.py`
- Unit testing using `pytest`
- Docstring documentation for all classes, methods, and constants
- IEEE-formatted references in source code and report
- Iterative development with descriptive Git commits

### Tech Stack
| Tool | Version |
|------|---------|
| Python | 3.14.2 |
| pip | 26.0.1 |
| pytest | 9.0.2 |
| IDE | Visual Studio Code |
| OS | Windows 11 |
| Version Control | Git + GitHub |

---

## Practical Project 3 — Flask MVC Web Application

**Branch:** `project3` | **Tag:** `V3.0` `V3.1` `V3.2` `V3.3`

### What Was Built
A fully functional MVC web application that migrated the terminal CRUD application from Project 2 into a browser-based interface using the Flask web framework. All existing business, persistence, and model layers were reused without modification.

### Architecture
```
View        →  presentation/templates/   (Jinja2 HTML templates)
Controller  →  presentation/routes.py    (Flask URL route functions)
Model       →  business/ + persistence/ + model/  (reused from Project 2)
```

### Folder Structure
```
PracticalProject03/
│   run.py
└── myapp/
    │   __init__.py
    ├── model/
    │       shorebird_monitoring_record.py
    ├── business/
    │       record_memory_storage.py
    ├── persistence/
    │       file_handler.py
    └── presentation/
        │   routes.py
        └── templates/
                base.html
                index.html
                view_one.html
                create.html
                edit.html
                delete.html
```

### Routes Implemented
| URL | Method | Feature |
|-----|--------|---------|
| `/` | GET | View all records |
| `/view/<index>` | GET | View one record |
| `/create` | GET / POST | Create a new record |
| `/edit/<index>` | GET / POST | Edit an existing record |
| `/delete/<index>` | GET / POST | Delete a record with confirmation |
| `/reload` | GET | Reload dataset from CSV file |
| `/save` | GET | Save records to UUID-named CSV file |

### Key Skills Demonstrated
- Flask MVC web framework setup and configuration
- Jinja2 templating — template inheritance, loops, conditionals, `url_for()`
- HTTP request handling — GET and POST methods
- Flask flash messaging with session cookie signing
- Refactoring a terminal application into a web application
- Reusing existing layered architecture with zero modification to lower layers
- HTML form design and user input handling
- Iterative Git commits per MVC layer

### Tech Stack
| Tool | Version |
|------|---------|
| Python | 3.14.3 |
| Flask | 3.1.3 |
| Werkzeug | 3.1.7 |
| Jinja2 | built into Flask |
| IDE | Visual Studio Code |
| OS | Windows 11 |
| Version Control | Git + GitHub |

---

## Practical Project 4 — Advanced Feature: Search & Filter

**Branch:** `project4` | **Tag:** `V4.0`

### What Was Built
An extension of the Project 3 Flask MVC web application with an advanced Search and Filter feature, allowing users to filter shorebird monitoring records by multiple columns simultaneously at runtime.

### Feature Selected
**Option B — Search or Filter records based on multiple columns at the same time**

### Filter Columns Supported
- Site Identification
- Area
- Visit Date

### Key Skills Demonstrated
- Extending an existing MVC web application with a new feature
- Multi-column filtering logic in the Business Layer
- Passing filter parameters via HTTP GET request query strings
- Cascading dropdown menus using Jinja2 templates
- Dynamic filtering of in-memory data without a database
- Iterative refactoring per MVC layer with Git commits per step

### Tech Stack
| Tool | Version |
|------|---------|
| Python | 3.14.3 |
| Flask | 3.1.3 |
| Werkzeug | 3.1.7 |
| Jinja2 | built into Flask |
| IDE | Visual Studio Code |
| OS | Windows 11 |
| Version Control | Git + GitHub |

---

## Skills Summary

| Category | Skills |
|----------|--------|
| **Languages** | Python 3.14 |
| **Web Framework** | Flask, Jinja2 |
| **Architecture** | N-Layered, MVC |
| **OOP Concepts** | Classes, Inheritance, Polymorphism, Encapsulation |
| **File Handling** | CSV read/write, UUID filename generation |
| **Testing** | pytest unit testing |
| **Version Control** | Git branching, commits, tagging, GitHub |
| **Documentation** | Python docstrings, IEEE-formatted references |
| **Tools** | Visual Studio Code, pip, Windows 11 |

---

## Repository Structure

```
CST8002_PracticalProject_010_AnnabelCheng/
├── PracticalProject01/
├── PracticalProject02/
├── PracticalProject03/
└── PracticalProject04/
```

---

## How to Run (Project 3 & 4)

```bash
# Clone the repository
git clone https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng.git

# Navigate to the project folder
cd PracticalProject03   # or PracticalProject04

# Install Flask
pip install flask

# Run the application
python run.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000
```

---

## Academic Integrity

All source code in this repository is the original work of Annabel Cheng, written as part of coursework at Algonquin College. External learning resources are documented using IEEE reference style within each source file and project report. AI writing assistance (Claude by Anthropic) was used to help format and polish docstring documentation only — all functional source code was written by the author.

---

*CST8002 Section 010 — Professor Stanley Pieda — Algonquin College, Winter 2026*
