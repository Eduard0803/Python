start: 
	@echo "\n\n\t\t----- installing dependencies -----\n\n"
	@pip install -r requirements.txt
	@sudo apt update
	@sudo apt install postgresql
	@sudo service postgresql start
	@python3 create_pdf.py
	@echo "\n\n\t\t----- starting server -----\n\n"
	@uvicorn server:app --reload
