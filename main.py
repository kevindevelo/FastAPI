from ast import While
from fastapi import FastAPI
from typing import List, Union
from pydantic import BaseModel

app = FastAPI()

class Index(BaseModel):
    index:int

def fibonacci_get(index:int) -> int:
    firt_number:int = 1;
    secondary_number:int = 1;
    counter:int = 1;
    out_index:int = 0

    while counter <= index:
        if counter == 1:
            counter +=1
            out_index = firt_number
        elif counter == 2:
            counter += 1
            out_index = secondary_number
        else:
            aux = firt_number + secondary_number
            firt_number, secondary_number = secondary_number, aux
            counter += 1
            out_index = aux
    
    return out_index





@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def get_hello():
    return {"response": "Hello FastAPI"}


@app.get("/isprime/{number}")
def validate_primo(number:int):
    assert type(number) == int, "Error, debe ingresar un numero";
    counter = 0;
    out = False;
    for i in range(1, number + 1):
            if(number % i != 0):
                continue
            counter +=1;
    
    if(counter == 2):
        out = True;
        
    return {"response": out}

@app.post("/fibonacci")
async def get_fibonacci(index:Index):
    if index.index <= 0:
        return {"response": "El parametro de entrada debe ser mayor a 0."}
    else:
        out = fibonacci_get(index.index)
        return {"response":out}
