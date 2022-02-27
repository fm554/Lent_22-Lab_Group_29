


def polyfit(dates, levels, p):
    """return a tuple of (i) the polynomial object and (ii) any shift of the time (date) axis
    
    Input arguments: dates, water levels, degree of polynomial"""
    import numpy as np

    # Create set of 10 data points on interval (0, 2)
    x = 
    y = 

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x, y, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    