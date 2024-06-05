import os
from io import BytesIO

import uvicorn
from fastapi import FastAPI, status, requests, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    os.makedirs("files", exist_ok=True)

@app.get("/")
def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "Hello World"
        }
    )

@app.post("/uploadfile/")
async def save_file(file: UploadFile):
    file_object = file.file
    file_object.seek(0)
    
    content_ = await file.read()
    content = BytesIO(content_)

    with open(f"files/{file.filename}", "wb") as f:
        f.write(content.getvalue())

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "filename": f"{file.filename} saved with success"
        }
    )

if __name__ == '__main__':
    uvicorn.run(
        app="server:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
