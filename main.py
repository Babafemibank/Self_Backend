from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
        title: str
        content: str
        published: bool = True
        rating: Optional[float] = None
        
my_post = [{
        "title": "title of post",
        "content":"content of post",
        "id": 1},{
        "title": "Favourite post",
        "content":"I like pizza",
        "id": 2}
           
           
           
           ]

@app.get("/")
async def root():
        return {"message": "Hello Babafemi! "}



@app.get("/post")
def get_post():
    return {"data": "This is a post endpoint"}


@app.post("/createposts")
def post(payload:Post):
        payload,dict()
        return {"data": payload.title, "title":payload.content, "published":payload.published, "rating":payload.rating}