from gateways.open_ai_gateway import open_ai_send_prompt

def generate_ai_response(text: str):
     prompt = (
        "You are an assistant replying over SMS. "
        "Your response will appear as a single text message on a user's phone. "
        "Be concise, direct, and under 160 characters. "
        "Do not add pleasantries like 'Hi' or 'Thanks'. "
        f"User: {text}"
    )
     response = open_ai_send_prompt(prompt)
     return response[:160]