from floodsystem.stationdata import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

# create some test data
test_station1 = MonitoringStation("1", "1", "1", [0, 0], [0, 1], "1", "1") 
test_station1.latest_level = 0.9

test_station2 = MonitoringStation("2", "2", "2", [2, 2], [0, 1], "2", "2") 
test_station2.latest_level = 2

test_station3 = MonitoringStation("3", "3", "3", [3, 3], [0, 1], "2", "2") 
test_station3.latest_level = 1.5


stations = [test_station1, test_station2, test_station3]
def test_stations_level_over_threshold():
    over_tol = stations_level_over_threshold(stations, 1.6)
    assert over_tol == [("2", 2.0)]

def test_stations_highest_rel_level():
    highest_rel = stations_highest_rel_level(stations, 2)
    assert highest_rel == [("2", 2.0), ("3", 1.5)]
