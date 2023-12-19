import pyotp
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from twilio.rest import Client


def send_code_in_call(name, number, code):
    account_sid = "your account_sid"
    auth_token = "your auth_token"
    twilio_number = "your twilio_number"

    client = Client(account_sid, auth_token)

    message = f"""<Response><Say language="pt-BR">
        Olá {name} o seu código de autenticação é {code}
        repetindo o seu código de autenticação é {code}
        </Say></Response>
    """

    call = client.calls.create(to=number, from_=twilio_number, twiml=message)


app = FastAPI()
templates = Jinja2Templates(directory="pages")

# Create the authentication code
secret_key = pyotp.random_base32()
totp = pyotp.TOTP(secret_key, interval=30)
secret_key = totp.now()


# Home Page
@app.get("/")
async def index(request: Request):
    # return the page 'home.html' rendered
    return templates.TemplateResponse("home.html", {"request": request})


# Route to recive user data
@app.post("/input", response_class=HTMLResponse)
async def qr(request: Request):
    form_data = await request.form()
    # get the user data
    name = form_data["name"]
    number = form_data["number"]
    # send the code on user's phone_number
    send_code_in_call(name, number, secret_key)

    # return the page 'code.html' rendered
    return templates.TemplateResponse("code.html", {"request": request})


# route to check the code
@app.post("/verify", response_class=HTMLResponse)
async def verify(request: Request):
    form_data = await request.form()
    # get the code that the user entered
    input = form_data["code"]
    if input == secret_key:
        # return the page 'success.html' rendered
        return templates.TemplateResponse("success.html", {"request": request})
    else:
        # return the page 'error.html' rendered
        return templates.TemplateResponse("error.html", {"request": request})
