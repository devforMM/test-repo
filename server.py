from fastapi import FastAPI
import asyncio

app=FastAPI()
pr

users=[
    
]


@app.get("/home")
def home():
    return  {"message":"welcome home"}


@app.get("/async")
async def my_function():
    await asyncio.sleep(10)
    return {"message":"function executed"}




@app.post("/register")
async def register(email:str,password: str,name: str,phone:str):
    await asyncio.sleep(10)
    users.append(
        {"email":email,
         "password":password,
         "name":name,
         "phone":phone}
    )
    return {"message":"user register successfully"}


