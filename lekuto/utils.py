import geocoder
from dotenv import load_dotenv
from os import getenv
load_dotenv()

def geocode(address):
    mapbox_api_key = getenv('MAPBOX_API_KEY')
    g = geocoder.mapbox(address, key=mapbox_api_key)
    return (g.json['lat'], g.json['lng'])
