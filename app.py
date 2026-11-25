from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="ООО Ромашка — бухгалтерский портал")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/api/status")
async def status():
    return {
        "status": "ok",
        "report": "Q4-reconciliation",
        "balance": 123456.78,
        "note": "TEST DATA ONLY",
    }


@app.post("/api/collect")
async def collect(payload: dict):
    print(f"[COLLECT] {payload}", flush=True)
    return {"received": True}
