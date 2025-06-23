from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import app

add = FastAPI()
add.mount("/static", StaticFiles(directory='./static'), name='static')
templates = Jinja2Templates('./templates')

@app.get('/')
def root(request: Request):
    return templates(request=request, name='index.html')

@app.get("/index2")
def index2(request: Request):
    return templates(request=request, name='index2.html')

@app.get('/test_json')
def test_json(request: Request):
    return {'test': 123}

@app.get("/test_json")

if __name__ == '__main__':
    uvicorn.run(app=app, port=880, host='192.168.88.65')