import json
from urllib import request
from urllib.parse import urlunsplit, urlencode

OSM_BASE_URL = "https://nominatim.openstreetmap.org/search"


def boot_up():
    '''
    for now just a raw example of how to query a forecast for a location
    by using a street address
    '''
    coords = get_lat_long("203 division st. bennington, vt")
    grid = get_grid(coords[0], coords[1])
    stations = get_stations(grid)
    # print(stations[0])
    observation = get_observation(stations[0]['properties']['stationIdentifier'])
    print(observation)


def get_lat_long(street_address: str) -> tuple:
    qry = urlencode(dict(
        format="json", addressdetails=1, polygon=1,
        q=street_address.strip()
    ))

    url = urlunsplit((
        'https', 'nominatim.openstreetmap.org', 'search',
        qry, ""
    ))

    with request.urlopen(url) as res:
        data = json.loads(res.read())
        # print(json.dumps(data, indent=4, sort_keys=True))
        return data[0]['lat'], data[0]['lon']


def get_grid(lat, long):
    url = urlunsplit((
        'https', 'api.weather.gov',
        'points' + '/' + lat + "," + long, None, None
    ))

    with request.urlopen(url) as res:
        data = json.loads(res.read())
        # print(json.dumps(data, indent=4, sort_keys=True))
        return (
            data['properties']['gridId'],
            data['properties']['gridX'],
            data['properties']['gridY'],
            data['properties']['observationStations']  # a fucking URL
        )


def get_forecast(grid):
    url = urlunsplit((
        'https', 'api.weather.gov',
        "gridpoints/" + str(grid[0]) + "/" + str(grid[1]) + "," + str(grid[2]) + "/forecast",
        None, None
    ))

    with request.urlopen(url) as res:
        data = json.loads(res.read())
        return data['properties']['periods']


def get_stations(grid):
    with request.urlopen(grid[3]) as res:
        data = json.loads(res.read())
        return data['features']


def get_observation(station_id):
    url = urlunsplit((
        'https', 'api.weather.gov',
        'stations/' + station_id + '/observations',
        None, None
    ))

    with request.urlopen(url) as res:
        data = json.loads(res.read())

        return data['features']
