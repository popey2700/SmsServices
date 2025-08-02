from logger import logger
from fastapi import APIRouter, Form, HTTPException, Header, Request, Response
from services.text_response_service import generate_text_response
from services.validation_service import is_valid_request
from twilio.twiml.messaging_response import MessagingResponse

router = APIRouter()

@router.post("/sms")
async def sms_webhook_controller(
    Body: str = Form(...),
    x_twilio_signature: str = Header(None),
    request: Request = None
    ):
    try:
        if await is_valid_request(request, x_twilio_signature):
            texts = generate_text_response(Body)
            twilio_response = MessagingResponse()
            for text in texts:
                twilio_response.message(text)
            return Response(content=str(twilio_response), media_type="application/xml")
        else:
            raise HTTPException(status_code=403, detail="Invalid Twilio signature")    
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"error": str(e)}, 500