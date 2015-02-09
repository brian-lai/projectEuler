countPrime = 1
currentPrime = 0
count = 2
while countPrime <= 10001:
    for i in range(2,count):
        if count%i == 0:
            if i == count:
                countPrime += 1
                currentPrime = count
            else:
                break
        count += 1
print currentPrime