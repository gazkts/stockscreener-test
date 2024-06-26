from typing import Union
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html",{
        "request": request
    })


@app.post("/stock")
def create_stock():
    return {
        "code": "success",
        "message": "stock created"
    }