# Qantas Junior Software Engineer Application Portfolio
[![Python CI](https://github.com/sophieleung007/qantas-job-demos/actions/workflows/python-tests.yml/badge.svg)](https://github.com/sophieleung007/qantas-job-demos/actions/workflows/python-tests.yml)
[![Render Deployment](https://img.shields.io/badge/Render-Deployed-success)](https://qantas-job-demos.onrender.com)

Demonstrating core technical skills required for Qantas Junior Software Engineer role through aviation-themed projects.

## 🌐 Live Demos
| Project | Live URL |
|---------|----------|
| **Flight Dashboard (HTML/JS/CSS)** | [https://sophieleung007.github.io/qantas-job-demos/](https://sophieleung007.github.io/qantas-job-demos/) |
| **Flask Web Application** | [https://qantas-job-demos.onrender.com/dashboard](https://qantas-job-demos.onrender.com/dashboard) |
| **CI/CD Unit Tests** | [GitHub Actions](https://github.com/sophieleung007/qantas-job-demos/actions/workflows/python-tests.yml) |

## 🛠️ Project Structure
```
.github/workflows/
  python-tests.yml       # CI/CD pipeline configuration
docs/
  index.html             # Flight Dashboard (GitHub Pages)
templates/
  dashboard.html         # Flask web interface
app.py                   # Flask web application
EmployeeManagement.java  # Java OOP demo
flights.sql              # SQL database schema
PaymentProcessor.java    # SOLID principles demo
requirements.txt         # Python dependencies
test_flight.py           # Unit tests
```

## 🚀 Running Projects Locally

### 1. Flight Dashboard (HTML/JS/CSS)
```bash
# Open directly in browser:
open docs/index.html
```

### 2. Flask Web Application
```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Access at: http://localhost:5000/login/Sophia
```

### 3. Java OOP Demo
```bash
javac EmployeeManagement.java
java EmployeeManagement
```

### 4. SOLID Principles Demo
```bash
javac PaymentProcessor.java
java Main
```

### 5. SQL Database Demo
```sql
-- Execute in PostgreSQL
\i flights.sql

-- Sample query
SELECT * FROM flights WHERE status = 'On Time';
```

### 6. Unit Tests
```bash
python test_flight.py

# Or through CI/CD:
git push origin main  # Triggers GitHub Actions
```

## 🔧 Technical Skills Demonstrated
| Skill Category | Technologies | Project Evidence |
|----------------|--------------|------------------|
| **Web Development** | HTML, CSS, JavaScript | Flight Dashboard (docs/index.html) |
| **Backend Framework** | Flask, REST APIs | app.py + templates |
| **OOP Principles** | Java | EmployeeManagement.java |
| **SOLID Principles** | Java | PaymentProcessor.java |
| **Database Design** | SQL | flights.sql |
| **Unit Testing** | Python unittest | test_flight.py |
| **CI/CD** | GitHub Actions | .github/workflows/python-tests.yml |

## 📈 CI/CD Pipeline
Automated testing configured via GitHub Actions:
```yml
name: Python CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.12'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run unit tests
      run: |
        python test_flight.py
```

## ✈️ Why Qantas?
Projects feature aviation themes demonstrating:
- Flight status tracking concepts
- Qantas brand colors (#e60000)
- Airline operational scenarios
- Travel industry data models

---

> "Be part of something special and play your part in the Qantas story"
