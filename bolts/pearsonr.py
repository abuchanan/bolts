from __future__ import division
import math

def pearsonr(x, y):
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    x_ss = 0
    y_ss = 0
    numerator = 0

    for xv, yv in zip(x, y):
        xr = xv - mean_x
        yr = yv - mean_y

        x_ss += xr * xr
        y_ss += yr * yr

        numerator += xr * yr

    denominator = math.sqrt(x_ss * y_ss)

    r = numerator / denominator
    return r
