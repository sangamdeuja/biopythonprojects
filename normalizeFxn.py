import math

def normalize(v):
    den=0
    for item in v:
        den=den+item*item
    return [i/math.sqrt(den) for i in v]


