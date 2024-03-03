def conejosR(n):
    if  n == 1 or n == 2:
        return n
    else:
        return conejosR(n - 1) +  conejosR(n - 2)
    
n = 11

print(conejosR(n))

