from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional,List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins= [
"http://localhost:8080",
"http://localhost",
"http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users = []
class User(BaseModel):
        imail: str
        isctive: bool
        bio : Optional[str]
@app.get("/")
async def root():
    return {"message" : "This simple back-end made from Ehsan for working with http method and api in front"}

@app.get("/users"  , response_model=List[User])
async def get_users():
    return users

@app.post("/users")
async def create_users(user : User):
    users.append(user)
    return "Succes"

@app.get("/users/{id}")
async def get_user(id: int= Path(...,description="The Id of User you want retrieve", gt=2),
                   isactive: str = Query(None,max_length=4)):
    return {"user": users[id] , "query" : isactive}

