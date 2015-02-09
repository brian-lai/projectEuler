import math

cap = 600851475143
cap = int(math.floor())
currentPrime = 29
condition = True

while condition:
    for i in range(2,cap):
        if cap%i == 0:
            if cap == 0:
                print cap
                condition = False
            else:
                break
    cap-=1