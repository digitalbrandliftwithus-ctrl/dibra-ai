
import os
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="DIBRA AI",
    description="AI Video Generator",
    version="1.0.0"
)

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)

app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/health")
async def health():
    return {
        "status": "online",
        "app": "DIBRA AI"
    }


@app.get("/api/status")
async def api_status():
    return {
        "app": "DIBRA AI",
        "video_generation": "Not connected yet",
        "message": "System ready"
    }
