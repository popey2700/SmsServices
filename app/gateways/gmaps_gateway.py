import requests
from config import GOOGLE_DIRECTIONS_API_KEY
from logger import logger

def get_gmaps_directions(origin: str, destination: str) -> str:
    try:
        url = "https://maps.googleapis.com/maps/api/directions/json"
        params = {
            "origin": origin,
            "destination": destination,
            "mode": "transit",
            "key": GOOGLE_DIRECTIONS_API_KEY
        }
        response = requests.get(url, params=params).json()
        return response
    except Exception as e:
        logger.error(f"Error: {e}")