from fastapi import FastAPI, Request, HTTPException
from crud import insert_person, query_person

app = FastAPI()

@app.get("/read/{name}/{age}/")
async def read(request: Request, name:str, age:int):

    content = query_person(name, age)

    if content is None:
        raise HTTPException(status_code=400, detail="Person not found")
    return {'name': name, 'age': age}

@app.post("/create/{name}/{age}/")
async def create(request: Request, name:str, age:int):
    
    if insert_person(name, age):
        return {'name': name, 'age': age}
    raise HTTPException(status_code=400, detail="Person data invalid")
