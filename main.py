from fastapi import FastAPI, Request, responses
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Форма связи")
templates = Jinja2Templates("./app/static")

app.mount("/images", StaticFiles(directory="./images"), name="images")

@app.get("/")
async def get_root(request: Request):
    return templates.TemplateResponse(request=request, name="about.html")

@app.get("/me")
async def get_otherpg(request: Request):
    return templates.TemplateResponse(request=request, name="me.html")

@app.get("/vhod")
async def get_otherpg(request: Request):
    return templates.TemplateResponse(request=request, name="vhod.html")

@app.get("/reg")
async def get_otherpg(request: Request):
    return templates.TemplateResponse(request=request, name="reg.html")

@app.get("/zak")
async def get_otherpg(request: Request):
    return templates.TemplateResponse(request=request, name="zak.html")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=80)