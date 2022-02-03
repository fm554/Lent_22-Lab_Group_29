from floodsystem.stationdata import build_station_list

from floodsystem.geo import rivers_with_station, stations_by_river


def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    # Part 1
    rivers = rivers_with_station(stations) # calls function defined in geo

    print (len(rivers), "rivers have at least 1 station. First 10 -", sorted(rivers)[:10])

    # Part 2
    rivers_stations = stations_by_river(stations) # calls function defined in geo

    print(sorted(rivers_stations['River Aire']))
    print(sorted(rivers_stations['River Cam']))
    print(sorted(rivers_stations['River Thames']))


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()