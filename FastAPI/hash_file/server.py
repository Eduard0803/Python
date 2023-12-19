from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from insert_file import query_file

app = FastAPI()
templates = Jinja2Templates(directory="pages")
app.mount("/static", StaticFiles(directory="pages/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def intial(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/auth", response_class=HTMLResponse)
async def form(request: Request, hash_code: str = Form()):
    content = query_file(hash_code)

    with open("pages/static/file_1.pdf", "wb") as file:
        file.write(content.file_content)

    return templates.TemplateResponse("index.html", {"request": request})
