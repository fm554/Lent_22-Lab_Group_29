from floodsystem.stationdata import build_station_list

from floodsystem.geo import stations_by_distance, rivers_with_station, stations_by_river

#1B test
def test_stations_by_distance():
    # Build list of stations
    stations = build_station_list()
    #generates full stations by distance list
    station_distances = stations_by_distance(stations, (52.2053, 0.1218))

    assert round(stations_by_distance[0][1], 2) == 0.84

#1C test

#1D test
def test_rivers_with_station():
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    assert len(rivers) < 0

def test_stations_by_river():
    stations = build_station_list()
    rivers_stations = stations_by_river(stations)
    assert len(rivers_stations['River Cam']) > 0

#1E test

