import cv2
from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse

app = FastAPI()


@app.get("/hello")
def read_root():
    return {"message": "Hello, world!"}


@app.get("/video-feed")
async def video_feed():
    cap = cv2.VideoCapture(0)

    async def generate():
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            ret, buffer = cv2.imencode(".jpg", frame)
            frame_bytes = buffer.tobytes()
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
            )

    return StreamingResponse(
        generate(), media_type="multipart/x-mixed-replace;boundary=frame"
    )


if __name__ == "__main__":
    import subprocess as sub

    sub.call(["uvicorn", "server:app", "--reload", "--host", "0.0.0.0"])
