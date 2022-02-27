from matplotlib import dates
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def plot_water_levels(station, dates, levels):
    """returns a plot of the water level data against time for a station
    
    Input arguments: stations(a list of Monitoring station objects), dates, water levels

    Returns: plot of water level against time"""
   

    t = [dates]
    levels = [station.latest_level]

    # Plot
    plt.plot(t, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("station")

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()
    
    
def plot_water_level_with_fit(station, dates, levels, p):
    """returns a plot of the water level data and the best-fit polynomial. 
    
    """
