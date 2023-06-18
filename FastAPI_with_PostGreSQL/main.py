from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from upload_data import upload_data
from get_data import get_data

app = FastAPI()
templates = Jinja2Templates(directory="pages")

@app.get("/", response_class=HTMLResponse) # the home page
async def intial(request: Request):
    return templates.TemplateResponse("initial_page.html", {"request": request})

@app.get("/sign-up", response_class=HTMLResponse) # register form
async def intial(request: Request):
    return templates.TemplateResponse("sign-up_form.html", {"request": request})

@app.post("/welcome", response_class=HTMLResponse) # welcome page
async def form(request: Request, name: str=Form(), age: int=Form(), email: str=Form(), password: str=Form()):
    upload_data(name, age, email, password) # upload the data_user to the data_bank
    # return {'name': name, 'age': age, 'email': email}
    return templates.TemplateResponse("welcome.html", {'request': request, 'name': name})

@app.get("/sign-in", response_class=HTMLResponse) # login form
async def intial(request: Request):
    return templates.TemplateResponse("sign-in_form.html", {"request": request})

@app.post("/process", response_class=HTMLResponse) # access page
async def form(request: Request, email: str=Form(), password: str=Form()):
    data_user = get_data(email, password) # get the data_user from the data_bank

    if not data_user or data_user[2] != email and data_user[3] != password:
        return templates.TemplateResponse("access_denied.html", {'request': request}) # access denied page
    return templates.TemplateResponse("access_allowed.html", {'request': request, # access allowed page
        'name': data_user[0], 'age': data_user[1], 'email': data_user[2], 'password': data_user[3]})
