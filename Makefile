packages = twilio\
			moviepy\
			pytube\
			pyautogui\
			opencv-python\
			speechrecognition\
			pyttsx3\
			fastapi\
			uvicorn\
			psycopg2

install:
	@for p in $(packages); do \
		pip install $$p; \
	done
