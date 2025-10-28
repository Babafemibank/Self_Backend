from fastapi import FastAPI, HTTPException, status, Response
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from dotenv import load_dotenv
import os
app = FastAPI()
load_dotenv()

class Post(BaseModel):
        title: str
        content: str
        published: bool = True
        rating: Optional[float] = None

try:
        conn = psycopg2.connect(host = os.getenv("host"),database=os.getenv("database"), user = 'postgres', password = os.getenv("password"))

my_post = [{
        "title": "title of post",
        "content":"content of post",
        "id": 1},{
        "title": "Favourite post",
        "content":"I like pizza",
        "id": 2},{
        "title": "title of post",
        "content":"content of post",
        "id": 3},{
        "title": "Favourite post",
        "content":"I like pizza",
        "id": 4},{
        "title": "title of post",
        "content":"content of post",
        "id": 5},{
        "title": "Favourite post",
        "content":"I like pizza",
        "id": 6},{
        "title": "title of post",
        "content":"content of post",
        "id": 7},{
        "title": "Favourite post",
        "content":"I like pizza",
        "id": 8}
           ]




@app.get("/")
async def root():
        return {"message": my_post}



@app.get("/post")
def get_post():
    return {"data": "This is a post endpoint"}


@app.post("/createposts")
def post(payload:Post):
        payload.dict()
        return {"data": payload.title, "title":payload.content, "published":payload.published, "rating":payload.rating}






def findpost(id):
      for p in my_post:
            if p["id"] == id:
                  return p
def findDelete(id):
       for index, p in enumerate(my_post):
              if p["id"] == id:
                     return index
@app.get("/")
async def root():
        return {"message": "Hello Babafemi! "}
@app.get("/post")
def get_post():
    return {"data": my_post}
@app.get("/post/{id}")
def getPost(id:int):
       post = findpost(id)
       if not post:
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"id {id} not found")
       return {"message": post}
@app.post("/createposts")
def post(payload:Post):
        post_dict = payload.dict()
        post_dict['id'] = randrange(0,100000)
        my_post.append(post_dict)
        print(my_post)
        return {"data": my_post}
@app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletePost(id: int):
       delete = findDelete(id)
       my_post.pop(delete)
       if delete == None:
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
@app.put('/post/{id}')
def updatePost(id: int, payload:Post):
       toupdate = findDelete(id)
       if toupdate == None:
              raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
       payload_dict = payload.dict()
       payload_dict["id"] = id
       my_post[toupdate] = payload_dict
       return {"data": my_post}







