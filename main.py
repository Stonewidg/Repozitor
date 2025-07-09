from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from utils import feedback_logger_to_file, validate_form_data
from db import db_con

app = FastAPI()
app.mount("/static", StaticFiles(directory='./app/static'), name='static')
templates = Jinja2Templates('./app/templates')

@app.get('/')
def root(request: Request):
    return templates(request=request, name='index.html')

@app.post('/feedback_form')
async def test_post(request: Request):
    form_data = await request.json()
    name = form_data['name']
    email = form_data['email']
    phone = form_data['phone']

    result_validate_data = validate_form_data(name, email, phone)

    if not result_validate_data['name']:
        return "Некоректное имя"
    elif not result_validate_data['email']:
        return"Некоректный email" 
    elif not result_validate_data['phone']:
        return "Некоректный номер телефона"
    else:
        str_for_logger = f'имя: {name}, Почта {email}, Номер телефона: {phone}'
        feedback_logger_to_file(str_for_logger)
        db_con.add_data(name, email, phone)
        return templates.TemplateResponse(request=request, name='success_form_status.html')

if __name__ == '__main__':
    uvicorn.run(app=app, port=80, host='192.168.88.59')