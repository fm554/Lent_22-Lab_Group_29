from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """returns stations with relative water level above tolerance

    Input arguments: stations(a list of Monitoring station objects), tol(float)

    Returns: list of tuples of form (name, relative water level)
    """
    over_tol = []
    for station in stations:
        if station.relative_water_level() != None:
            if station.relative_water_level() > tol:
                over_tol.append((station.name, station.relative_water_level()))

    over_tol = sorted_by_key(over_tol, 1, reverse=True)
    return over_tol
        
    
def stations_highest_rel_level(stations, N):
    """returns N stations with highest relative water level 

    Input arguments: stations(a list of Monitoring station objects), N(int)

    Returns: list of tuples of form (name, relative water level)
    """
    sorted_stations = stations_level_over_threshold(stations, 0)
    return sorted_stations[:N]