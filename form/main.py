from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# print the home interface
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # return the file 'index.html' rendered
    return templates.TemplateResponse("index.html", {"request": request})

# recive the data from the form
@app.get("/input", response_class=HTMLResponse)
async def show_form():
    with open("input.html") as f:
        content = f.read()
    return HTMLResponse(content=content)

# print the data in the endpoint '/out'
@app.post("/out")
async def process_form(request: Request):
    form_data = await request.form()
    name = form_data['name']
    age = form_data['age']
    email = form_data['email']

    # create the .json file
    data = {'name': name, 'age': age, 'email': email}
    with open('data.json', 'a') as file:
        json.dump(data, file)
    
    # return the file 'output.html' rendered
    return templates.TemplateResponse("output.html", {"request": request, "name": name, "age": age, "email": email})
