
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import find_station_from_name
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime




def run():
    """Requirements for Task 2E"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    highest5 = stations_highest_rel_level(stations, 5)

    for station_data in highest5:
        station_name = station_data[0]
        station = find_station_from_name(station_name, stations)
        dt = 10
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        if dates == [] or levels == []:
            print("no data at", station_name)
        else:
            plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()