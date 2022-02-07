from floodsystem.stationdata import build_station_list

from floodsystem.geo import rivers_by_station_number

def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = build_station_list()

    #generates first nine rivers by the number of stations they have
    number_stations_river= rivers_by_station_number(stations, 9)
   
   #print output
    print(number_stations_river)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()