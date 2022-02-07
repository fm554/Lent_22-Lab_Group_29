# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

# Task 1B
def stations_by_distance(stations, p):
    """returns all stations sorted by distance from coordinate 

    Input arguments: stations(a list of Monitoring station objects), p(lat, lon)

    Returns: list of tuples of form (name, town, distance)

    """
    
    station_distance = []
    # calculate and append haversine distances
    for station in stations:
        distance = haversine(station.coord, p)
        station_distance.append((station.name, station.town, distance))
    #sort by key
    station_distance = sorted_by_key(station_distance, 2)
    return station_distance

# Task 1C
def stations_within_radius(stations, centre, r):
    """returns all stations within a radius of a coordinate

    Input arguments: stations(a list of Monitoring station objects), centre(lat, lon), r(distance in Km)
   
    Returns: list of tuples of form (name)"""
    station_in_radius= []
    for station in stations:
        distance2= haversine(station.coord, centre)
        if distance2<=r:
         station_in_radius.append((station.name))
    station_in_radius= sorted(station_in_radius)
    return station_in_radius     



# Task 1D
def rivers_with_station(stations):
    """"returns a set with a list of non duplicate rivers with monitoring stations

    Input arguments: stations (a list of Monitoring Station objects)

    Returns: Set
    """
    rivers = set() #set means no requirement to check for duplicates
    for station in stations:
        rivers.add(station.river)

    return rivers

def stations_by_river(stations):
    """"maps river names to the list of station objects on a given river

    Input arguments: stations (a list of Monitoring Station objects)

    Returns: Dictionary {River: [list of monitoring stations on that river]]}
    """
    rivers = rivers_with_station(stations) #reuses previous function
    rivers_stations = {}
    #iterate through rivers and stations to generate each key-value pair
    for river in rivers:
        river_stations = []
        for station in stations:
            if station.river == river: #check if the station's river matches the current
                river_stations.append(station.name)
        rivers_stations[river] = river_stations
    return rivers_stations

#task 1E
def rivers_by_station_number(stations, N):
    """determines the N rivers with the greatest number of monitoring stations
    
    Input arguments: stations (a list of Monitoring Station object), N(number of rivers)
    
    Returns: list of tuples of form (river, number of stations)"""


    
    rivers_by_station_number=[]
    rivers=[]
    for station in stations:
        rivers.append(station.river)
    
    for river in rivers:
      rivers_by_station_number.append((river, (rivers.count(river)))) #iterating through rivers and counting the number of duplicate entries indicating each station
      rivers_by_station_number_sorted=tuple(set(rivers_by_station_number)) #removing duplicates
      rivers_by_station_number_sorted2=sorted_by_key(rivers_by_station_number_sorted, 1, reverse=True) #sorting by number of stations
      if N<1:
          print("error: N must be greater than 0")
      N_stations=rivers_by_station_number_sorted2[:N]
    
    
    return N_stations