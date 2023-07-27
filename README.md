# geoquery

#### query a weather observation or forecast for a given location.

an example run:

``` python
# get coordinates
coords = get_lat_long("203 division st. bennington, vt")
'''
acquire the grid based on coordinates
NWS API looks up stations by grid, not by lat./long.
'''
grid = get_grid(coords[0], coords[1])
# get all the stations within grid
stations = get_stations(grid)
'''
grab a station identifier from the stations list
to retrieve a weather observation
'''
observation = get_observation(stations[0]['properties']['stationIdentifier'])
print(observation)
```