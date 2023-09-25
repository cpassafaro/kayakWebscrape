from kayak import *
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
  return {"Hello world!"}

@app.get("/all-kayaks")
def getAll():
  return getAllKayaks()

@app.get("/company/{name}")
def getByCompany(name: str):
  if name == 'next-adventure':
    return getBoatsNA()
  if name == 'colorado-kayak':
    return getBoatsFromColoradoKayak()
  if name == 'rutabaga-shop':
    return getBoatsFromRutabaga()