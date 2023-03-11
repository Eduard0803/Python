from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json, os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/icons", StaticFiles(directory="icons"), name="icons")

@app.get('/', response_class=HTMLResponse)
def test():
    with open('templates/index.html') as f:
        content = f.read()
    return HTMLResponse(content=content)

@app.get('/form', response_class=HTMLResponse)
def test():
    with open('templates/form.html') as f:
        content = f.read()
    return HTMLResponse(content=content)

@app.post("/form-result")
async def process_form(request: Request):
    form_data = await request.form()
    name = form_data['nome']
    email = form_data['email']
    message = form_data['mensagem']

    with open('body.txt', 'w') as file:
        file.write(f'nome: {name}<br>email: {email}<br>menssagem: {message}<br>')
    os.system('./email.exe')

    return templates.TemplateResponse("result.html", {"request": request, "nome": name, "email": email, "mensagem": message})
