from math import gcd
def coins(c1,c2):
    return -1 if gcd(c1,c2)!=1 else (c1-1) * (c2-1)-1


print(coins(2,4))