from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from send_email import send_email

app = FastAPI()
app.mount("/static", StaticFiles(directory="pages/static/"), name="static")
templates = Jinja2Templates(directory="pages")

@app.get('/', response_class=HTMLResponse) # the initial page
async def home_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.post('/get_data', response_class=HTMLResponse) # the post method
async def get_data(request: Request, name: str=Form(), email: str=Form(), phone: str=Form(), message: str=Form()):
    # send the email with data user
    send_email(name, email, phone, message)
    return RedirectResponse("/", status_code=303)
