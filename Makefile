venv:
	virtualenv -p python3.9 venv3.9

install:
	pip install -r requirements.txt

env:
	cp .env.example .env

start:
	uvicorn app.main:app --port 8080 --reload