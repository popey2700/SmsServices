from gateways.open_ai_gateway import open_ai_send_prompt

def generate_ai_response(text):
    prompt = (
        "You are an assistant replying over SMS. "
        "Your response will appear as a single text message on a user's phone. "
        "Be concise, direct, and under 160 characters. "
        "Do not add pleasantries like 'Hi' or 'Thanks'. "
        f"User: {text}"
    )
    return open_ai_send_prompt(prompt)

def ai_format_directions_steps(steps_data):
    known_places = [
        "120 scylla road, se15 3rz",
        "26 rushworth st, se1 0rb",
        "Elephant & Castle Station",
        "London Bridge Station",
        "Peckham Rye Station",
        "Nunhead Station"
    ]
    
    prompt = (
        "Format the following travel directions into a clean, easy-to-read SMS. "
        "Be concise but include key streets, stops, and durations. "
        "Do not use extra greetings.\n\n"
        f"The user is familiar with these locations: {', '.join(known_places)}.\n"
        "If the goal of a walking section is simply to reach one of these locations, "
        "replace that entire walking section with: 'Go to <location>'.\n\n"
        f"Steps: {steps_data}"
    )

    return open_ai_send_prompt(prompt)