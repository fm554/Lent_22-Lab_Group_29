from floodsystem.analysis import polyfit
from floodsystem.stationdata import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import numpy



def test_polyfit():
    stations = build_station_list()
    update_water_levels(stations)
    station=stations[25]
    dt=3
    dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
    poly, shift= polyfit(dates, levels, 4)
    assert type(poly)==numpy.poly1d




