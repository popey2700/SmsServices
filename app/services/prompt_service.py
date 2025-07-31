from gateways.open_ai_gateway import open_ai_send_prompt

def generate_ai_response(text: str):
     prompt = f"Answer in under 160 chars: {text}"
     response = open_ai_send_prompt(prompt)
     return response