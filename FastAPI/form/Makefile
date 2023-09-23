install:
	@echo "\n\n\t\t----- installing dependencies -----\n\n"
	@pip install -r requirements.txt

start:
	@echo "\n\n\t\t----- starting server -----\n\n"
	@uvicorn server:app --reload

stop:
	@pkill -f "uvicorn myapp:app --host 0.0.0.0 --port 8000" || true
