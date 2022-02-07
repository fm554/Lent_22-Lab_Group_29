from floodsystem.stationdata import build_station_list

from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number

#1B test
def test_stations_by_distance():
    # Build list of stations
    stations = build_station_list()
    #generates full stations by distance list
    station_distances = stations_by_distance(stations, (52.2053, 0.1218))

    assert round(station_distances[0][2], 2) == 0.84

#1C test
def test_stations_within_radius():
    # Build list of stations
    stations = build_station_list()
    stations_in_range = stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert len(stations_in_range)>0


#1D test
def test_rivers_with_station():
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    assert len(rivers) > 0

def test_stations_by_river():
    stations = build_station_list()
    rivers_stations = stations_by_river(stations)
    assert len(rivers_stations['River Cam']) > 0

#1E test
def test_rivers_by_station_number():
     # Build list of stations
    stations = build_station_list()
    number_stations_river= rivers_by_station_number(stations, 10)
    assert len(number_stations_river)>=10
