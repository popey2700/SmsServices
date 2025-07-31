from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.sms_controller import router as sms_webhook_controller

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lock this down later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sms_webhook_controller)