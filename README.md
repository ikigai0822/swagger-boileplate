# Flask + Swagger Boilerplate

This is a minimal, production-ready boilerplate for building REST APIs using **Flask** and **Swagger UI** via [Flasgger](https://github.com/flasgger/flasgger). It's the fastest way to get interactive API docs in your Flask project.

---

## Tech Stack

- **Flask** — Web microframework
- **Flasgger** — Auto-generates Swagger UI (OpenAPI 2.0 & 3.0 compatible)

---

## Project Structure

├── app.py # Main application code
├── requirements.txt # Python dependencies
├── .gitignore # Git exclusions
├── README.md # This file
└── docs/
└── greet.yaml # OpenAPI 3.0 docs for /greet

## Getting Started

### 1. Clone the repo

bash
git clone https://github.com/your-username/flask-swagger-boilerplate.git
cd flask-swagger-boilerplate

## 2. Create A Python Virtual environemnt or use pipx

pip install -r requirements.txt

python3 app.py

## 3. Voila check localhost:8000/apidocs for swagger