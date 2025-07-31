from fastapi import APIRouter, Form
from services.prompt_service import generate_ai_response
from twilio.twiml.messaging_response import MessagingResponse

router = APIRouter()

@router.post("/sms")
async def sms_webhook_controller(Body: str = Form(...)):
    try:
        ai_response = generate_ai_response(Body)
        twilio_response = MessagingResponse()
        twilio_response.message(ai_response)
        return str(twilio_response)
    except Exception as e:
        return {"error": str(e)}, 500