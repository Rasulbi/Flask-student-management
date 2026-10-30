# Flask Student Management System

A beginner-friendly Flask application that lets you add, view, and delete student records. Data is stored in a local SQLite database.

## Requirements
- Python 3.9 or newer
- pip

## Setup

### Windows
```bash
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

### Linux / macOS / WSL
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Run tests
```bash
pytest -v
```

## Project structure
```text
flask-student-management/
├── app.py
├── requirements.txt
├── tests/
│   └── test_app.py
├── templates/
│   ├── index.html
│   └── add_student.html
└── static/
    └── style.css
```

The SQLite database (`students.db`) is created automatically when the app runs.
