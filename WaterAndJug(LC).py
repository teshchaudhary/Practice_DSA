def gcd(a,b):
    if b == 0:
        return a
    
    return gcd(b,a%b)

def canMeasureWater(jug1Capacity,jug2Capacity,targetCapacity):
    if targetCapacity == 0:
        return True
    
    if jug1Capacity + jug2Capacity < targetCapacity:
        return False
    
    return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0

