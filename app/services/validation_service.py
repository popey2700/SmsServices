from fastapi import Request
from config import TWILIO_AUTH_TOKEN
from twilio.request_validator import RequestValidator

async def is_valid_request(request: Request, x_twilio_signature: str):
    validator = RequestValidator(TWILIO_AUTH_TOKEN)
    form_data = await request.form()
    return validator.validate(
        str(request.url), form_data, x_twilio_signature
    )