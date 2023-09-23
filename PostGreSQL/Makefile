install: 
	@echo "\n\n\t\t----- installing dependencies -----\n\n"
	@pip install -r requirements.txt
	@sudo apt update
	@sudo apt install postgresql

start:
	@sudo service postgresql start

status:
	@sudo service postgresql status

stop:
	@sudo service postgresql stop
