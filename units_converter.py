"""
A units converter that can convert MPG to KPL
"""

# Useful constants
kpm = 1.60934
gpl = 0.264172
mpk = 0.621371
lpg = 3.78541
def mpg2kpl(mpg):
    return round(mpg * kpm * gpl, 4)
def kpl2mpg(kpl):
    return round(mpk * lpg * kpl, 4)