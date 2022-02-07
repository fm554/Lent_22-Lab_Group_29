from floodsystem.stationdata import build_station_list

from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""
   
    # Build list of stations
    stations = build_station_list()

    stations_in_range=stations_within_radius(stations, (52.2053, 0.1218), 10)

    print(stations_in_range)
   



if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()