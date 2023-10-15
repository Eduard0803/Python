from fastapi import FastAPI, Request, HTTPException
from crud import insert_person, query_person, update_person, delete_person
from pydantic import BaseModel, EmailStr

class Person(BaseModel):
    email: EmailStr
    name: str
    age: int

app = FastAPI()

@app.post('/person/')
async def create(request: Request, person: Person):

    insert_person(person)
    raise HTTPException(status_code=200, detail="person data entered")
    # raise HTTPException(status_code=400, detail="person data invalid")

@app.get('/person/{email}/')
async def read(request: Request, email:str):

    content = query_person(email)

    if content is None:
        raise HTTPException(status_code=400, detail="person not found")
    return {'name': content.name, 'email': content.email, 'age': content.age}

@app.put('/person/')
async def update(request:Request, person:Person):

    if update_person(person):
        return HTTPException(status_code=200, detail='update success')
    return HTTPException(status_code=400, detail='update error')

@app.delete('/person/{email}/')
async def delete(request: Request, email:str):

    if delete_person(email):
        return HTTPException(status_code=200, detail='successfully deleted')
    return HTTPException(status_code=400, detail='error when deleting')
