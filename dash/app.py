from dash import Dash, html
import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import Dash, html
import requests
import json

response = requests.get('http://app:5000/')
data = json.loads(response.text)

app = Dash(__name__)
app.layout = html.Div([
    dl.Map([
        dl.TileLayer(),
        dl.GeoJSON(data=dlx.dicts_to_geojson([
            {'lat': d['latitude'], 'lon': d['longitude']} for d in data]), 
                cluster=True)],
        id="map", zoom=1, style={'width': '100%', 
        'height': '50vh', 'margin': "auto", "display": "block"})
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050)
