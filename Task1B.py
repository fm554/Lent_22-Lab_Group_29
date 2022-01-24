from floodsystem.stationdata import build_station_list

from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()



    # Display data from 3 stations:
    for station in stations:
        if station.name in [
                'Bourton Dickler', 'Surfleet Sluice', 'Gaw Bridge'
        ]:
            print(station.coord)



if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()