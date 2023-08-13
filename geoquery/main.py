from geoquery.geode import get_lat_long, get_grid, get_stations, get_observation

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
