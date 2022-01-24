# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    #iterate through stations appending names and haversine distances
    station_distance = []
    for station in stations:
        distance = 10 * station.coord
        station_distance.append(station.name, distance)
    #sort by key


    return
