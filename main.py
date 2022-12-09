from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class DataBase(BaseModel):
    user_id = int
    user_name = str
    user_email = str
    user_message = str


@app.post('/data')
def data_record(request: DataBase):
    return f'{request.user_id} Is Your Id {request.user_name} {request.user_email} {request.user_message}'


@app.get('/')
def main(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "id": id})

