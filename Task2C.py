from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2C"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations_highest_rel_level(stations, 10):
        print(station[0], station[1])



if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
