import numpy as np
import matplotlib as plt

def polyfit(dates, levels, p):
    """return a tuple of (i) the polynomial object and (ii) any shift of the time (date) axis
    
    Input arguments: dates, water levels, degree of polynomial"""
    
    x = plt.dates.date2num(dates)
    shift = x[0]
    p_coeff = np.polyfit(x - shift, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, shift
    