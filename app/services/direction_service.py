import html
from pydantic import Json
from logger import logger
from gateways.gmaps_gateway import get_gmaps_directions

def generate_directions(text: str):
    try:
        direction_query_details = get_direction_query_details(text)
        origin = direction_query_details[0].strip()
        destination = direction_query_details[1].strip()
        raw_gmaps_directions_json= get_gmaps_directions(origin, destination)
        return format_directions(raw_gmaps_directions_json)
    except Exception as e:
        logger.error(f"Error: {e}")


def get_direction_query_details(text: str) -> str:
    return text[len("directions"):].strip().split(" to ")

def format_directions(directions_raw_json: Json) -> str:
    steps = directions_raw_json["routes"][0]["legs"][0]["steps"]

    instructions = []
    for step in steps:
        instruction = html.unescape(step["html_instructions"])
        duration = step.get("duration", {}).get("text", "")

        if step["travel_mode"] == "TRANSIT":
            transit_details = step.get("transit_details", {})
            dep_stop = transit_details.get("departure_stop", {}).get("name", "")
            arr_stop = transit_details.get("arrival_stop", {}).get("name", "")
            line = transit_details.get("line", {}).get("short_name", transit_details.get("line", {}).get("name", ""))
            instruction = f"Train {line} from {dep_stop} to {arr_stop}"

        instructions.append(f"{instruction} ({duration})")

    return " → ".join(instructions)