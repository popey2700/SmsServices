from ast import Tuple
from logger import logger
from pydantic import Json
from services.prompt_service import ai_format_directions_steps
from gateways.gmaps_gateway import get_gmaps_directions

def generate_directions(text: str):    
    try:
        origin, destination = get_direction_query_details(text)
        origin = resolve_known_place(origin)
        destination = resolve_known_place(destination)
        raw_gmaps_directions_json= get_gmaps_directions(origin, destination)
        return format_directions(raw_gmaps_directions_json)
    except Exception as e:
        logger.error(f"Error: {e}")

def get_direction_query_details(text: str) -> Tuple:
    direction_query_details = text[len("dir"):].strip().split(" to ")
    return (direction_query_details[0].strip(), direction_query_details[1].strip())

def resolve_known_place(place: str) -> str:
    known_places_map = {
        "home": "120 scylla road, se15 3rz",
        "work": "26 rushworth st, se1 0rb",
    }
    lower = place.strip().lower()
    return known_places_map.get(lower, place)

def format_directions(directions_raw_json: Json) -> str:
    steps = directions_raw_json["routes"][0]["legs"][0]["steps"]
    steps_data = []
    for step in steps:
        if step["travel_mode"] == "TRANSIT":
            steps_data.append({
                "mode": "TRANSIT",
                "instruction": step["html_instructions"],
                "duration": step["duration"]["text"],
                "details": step.get("transit_details", {})
            })
        elif step["travel_mode"] == "WALKING":
            sub_steps = step.get("steps", [])
            steps_data.append({
                "mode": "WALKING",
                "instruction": step["html_instructions"],
                "duration": step["duration"]["text"],
                "sub_steps": [s["html_instructions"] for s in sub_steps]
            })
    return ai_format_directions_steps(steps_data)