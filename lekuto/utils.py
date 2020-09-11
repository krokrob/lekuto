import geocoder

def geocode(address):
    mapbox_api_key = 'pk.eyJ1Ijoia3Jva3JvYiIsImEiOiJjam83MjVrbWkwbWNoM3FwN2VhMm81eGRzIn0.yM3wkq5LJd8NeSYyPyTY4w'
    g = geocoder.mapbox(address, key=mapbox_api_key)
    return (g.json['lat'], g.json['lng'])
