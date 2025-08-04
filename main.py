from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Форма связи")

app.mount("/index", StaticFiles(directory='./app/static'))
templates = Jinja2Templates("./app/static")

@app.get("/")
async def get_root(request: Request):
    return templates.TemplateResponse(request=request, name="about.html")

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.88.59", port=80)