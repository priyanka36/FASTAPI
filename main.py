from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {"data":"bloglist"}


@app.get('/blog')
def unpublished(limit:int=20,published:bool = True,sort:Optional[str]=None):
    if published:
        return{"data":f"{limit}all unpublished blogs{published}"}

@app.get('/blog/{id}')
def index(id:int):
    return{"data":{"name":id}}



@app.get('/blog/{id}/comments')
def comments(id,limit=10):
    return{"data":{'comments':{id}}}

@app.post('/blog')
def create_blog():
    return {'data':"Blog is created"}

class Blog (BaseModel):
    title:str 
    body:str
    published:Optional[bool]
    pass 

@app.post("/blog")
def create_blog(request:Blog):
    
    return request
    return {'data':f"Blog is created with title as {request.title}"}