import matplotlib.pyplot as plt
import matplotlib
from .analysis import polyfit
import numpy as np

def plot_water_levels(station, dates, levels):
    """returns a plot of the water level data against time for a station
    
    Input arguments: stations(a list of Monitoring station objects), dates, levels (a list of floats)

    Returns: plot of water level against time"""

    # Plot
    plt.plot(dates, levels)
    plt.axhline(y = station.typical_range[0], color='r')
    plt.axhline(y = station.typical_range[1], color='r')
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()
    
def plot_water_level_with_fit(station, dates, levels, p):
    """returns a plot of the water level data and the best-fit polynomial. 
    
    Input arguments: station (a list of Monitoring station objects), dates, levels(list of floats), p (integer)"""

    poly, shift = polyfit(dates, levels, p)

    # Plot
    x = matplotlib.dates.date2num(dates)
    x1 = np.linspace(shift, x[-1], 30)
    plt.plot(x, levels)
    plt.plot(x1, poly(x1 - shift))
    plt.axhline(y = station.typical_range[0], color='r')
    plt.axhline(y = station.typical_range[1], color='r')

    plt.ylabel('water level (m)')
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()
