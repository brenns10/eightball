.PHONY: init server

init:
	virtualenv -p python3.6 venv
	venv/bin/pip install -r requirements.txt
	
server:
	FLASK_APP=eightball.py venv/bin/flask run --host=0.0.0.0 --port=25430
