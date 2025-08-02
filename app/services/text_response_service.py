from services.prompt_service import generate_ai_response
from services.direction_service import generate_directions

def generate_text_response(text: str):
    text = text.lower()
    if text.startswith("dir"):
         return generate_directions(text)

    return generate_ai_response(text)
