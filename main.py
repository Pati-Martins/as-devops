from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message": "olá"}

@app.get("/funcaoteste")
async def funcaoteste():
    return{"teste": True, "num_aleatorio": random.randint(0, 1000)}
