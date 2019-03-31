import math

def normalize(v):
    den=0
    for item in v:
        den=den+item*item
    return [i/math.sqrt(den) for i in v]


def cosine_sim(v1,v2):
    sum=0
    vec1=normalize(v1)
    vec2=normalize(v2)
    for i in range(0,len(vec1)):
        sum=sum+vec1[i]*vec2[i]
    return sum
