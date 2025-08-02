from services.prompt_service import generate_ai_response
from services.direction_service import generate_directions

def generate_text_response(text: str):
    text = text.lower()
    if text.startswith("directions"):
        response = generate_directions(text)
    else:
        response = generate_ai_response(text)

    texts = split_into_sms_chunks(response) 
    return texts

def split_into_sms_chunks(message: str) -> list[str]:
    max_length: int = 160
    chunks = [message[i:i + max_length] for i in range(0, len(message), max_length)]

    if len(chunks) > 1:
        chunks = [f"({i+1}/{len(chunks)}) {chunk}" for i, chunk in enumerate(chunks)]

    return chunks
