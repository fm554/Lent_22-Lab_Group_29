from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import numpy as np
import matplotlib as plt


def trend_up(station):
        dt = 1
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        if dates == [] or levels == []:
            return None
        x = plt.dates.date2num(dates)
        shift = x[0]
        m, c = np.polyfit(x - shift, levels, 1)
        if m > 0:
            return True
        elif m < 0:
            return False

def run():
    """To determine whether a town is at severe, high, moderate or low risk, we use two markers -  
    1) Whether the latest level is outside the typical range
    2) The trend line using a polynomial of order 1"""

    stations = build_station_list()
    update_water_levels(stations)

    # generate variables
    towns = set()
    severe_towns = []
    high_towns = []
    moderate_towns = []
    low_towns = []

    # generate town list
    for station in stations:
        towns.add(station.town)
    
    # sort through towns and check for risk factors
    towns2 = list(towns)[:100]
    for town in towns2:
        count = 0
        score = 0
        for station in stations:
            if station.town == town:
                count += 1
                if type(station.relative_water_level()) != float:
                    count -= 1
                elif station.relative_water_level() >= 1:
                    if trend_up(station) == True:
                        score += 3
                    elif trend_up(station) == False:
                        score += 2 
                    elif trend_up(station) == None:
                        count -= 1                     
                elif station.relative_water_level() < 1:
                    if trend_up(station) == True:
                        score += 1
                    elif trend_up(station) == False:
                        score += 0 
                    elif trend_up(station) == None:
                        count -= 1    
                else:
                    print("Unexpected relative water level")

        
        if count == 0:
            count += 1
        # calculate town risk
        risk = round(score/count)
        print(risk, town)
        # add town to relevant list
        if risk == 0:
            low_towns.append(town)
        elif risk == 1:
            moderate_towns.append(town)
        elif risk == 2:
            high_towns.append(town)
        elif risk == 3:
            severe_towns.append(town)

    print ("Severe Risk Towns Include:", severe_towns[:10])
    print ("High Risk Towns Include:", high_towns[:10])
    print ("Moderate Risk Towns Include:", moderate_towns[:10])
    print ("Low Risk Towns Include:", low_towns[:10])

if __name__ == "__main__":
    print("*** Task 2G CUED Part IA Flood Warning System ***")
    run()

            












    



if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()