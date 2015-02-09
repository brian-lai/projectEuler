start = 2520
condition = True
flag = 0
#primes = [2,3,5,7,11,13,17,19]

while condition:
    for i in range(1,21):
        if start%i > 0:
            flag = 0
            break
        else:
            flag = 1
    if flag == 1:
        print start
        condition = False
    else:
        start += 1
