# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


def stations_by_distance(stations, p):
    """returns all stations sorted by distance from coordinate 

    Input arguments: stations(from build_station_list), p(lat, lon)

    Returns: list of tuples of form (name, town, distance)

    """
    
    station_distance = []
    for station in stations:
        distance = haversine(station.coord, p)
        station_distance.append((station.name, station.town, distance))
    #sort by key
    station_distance = sorted_by_key(station_distance, 2)
    return station_distance
