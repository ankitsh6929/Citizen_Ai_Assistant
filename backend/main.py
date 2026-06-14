from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.chat import router as chat_router
from backend.routes.voice import router as voice_router

app = FastAPI()

app.mount(
    "/audio",
    StaticFiles(directory="."),
    name="audio"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://13.222.185.113:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(voice_router)