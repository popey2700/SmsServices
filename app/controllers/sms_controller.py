import logging

from fastapi import APIRouter, Form
from services.prompt_service import generate_ai_response
from twilio.twiml.messaging_response import MessagingResponse

router = APIRouter()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@router.post("/sms")
async def sms_webhook_controller(Body: str = Form(...)):
    try:
        logger.info(f"Incoming SMS: {Body}")
        ai_response = generate_ai_response(Body)
        logger.info(f"GPT Reply: {ai_response}")
        twilio_response = MessagingResponse()
        twilio_response.message(ai_response)
        return str(twilio_response)
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"error": str(e)}, 500