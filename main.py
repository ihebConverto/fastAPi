from fastapi import FastAPI
from models import Blogs
from mongoengine import connect
from pydantic import BaseModel
import json
from fastapi import FastAPI
from bson.objectid import ObjectId
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
connect(db="blogapi" , host="localhost" , port=27017)

origins = [
    "http://127.0.0.1:8080",
    "https://localhost:8080",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Our root endpoint
@app.get("/")
def index():
    return {"message": "Welcome to FastAPI World"}

@app.get("/blogs")
def blogs():
    blogs=Blogs.objects().to_json()
    blogs_list=json.loads(blogs)
    return {"blogs":blogs_list}

@app.get("/get_blog/{id}")
def get_blogs(id):
    blog=Blogs.objects.get(id=id)
    blogs_dic={
        "id":id,
        "title":blog.title,
        "author":blog.author,
        "body":blog.body,
        "likes":blog.likes,
        "dislikes":blog.dislikes,

    }

    return blogs_dic

class newBlog(BaseModel):
    title:str
    author:str
    body:str
    likes:int
    dislikes:int

@app.post("/add_blog")
def add_blog(blog:newBlog):
    new_blog=Blogs(
                    title=blog.title,
                    author=blog.author,
                    body=blog.body,
                    likes=blog.likes,
                    dislikes=blog.dislikes)
    new_blog.save()

    return {"message":"Blog successfully added"}

class updateBlog(BaseModel):
    title:str
    author:str
    body:str
    likes:int
    dislikes:int

@app.get("/likes/{id}")
def update_blogs(id):
    blog=Blogs.objects.get(id=id)
    blog.likes=blog.likes+1
    blog.save()
    blogs_dic={
        "id":id,
        "title":blog.title,
        "author":blog.author,
        "body":blog.body,
        "likes":blog.likes,
        "dislikes":blog.dislikes,

    }

    return blogs_dic


@app.get("/dislikes/{id}")
def update_blogs(id):
    blog=Blogs.objects.get(id=id)
    blog.dislikes=blog.dislikes+1
    blog.save()
    blogs_dic={
        "id":id,
        "title":blog.title,
        "author":blog.author,
        "body":blog.body,
        "likes":blog.likes,
        "dislikes":blog.dislikes,

    }

    return blogs_dic
