count = 3
total = 0

while count < 2000000:
    for i in range(2,count):
        if count%i == 0:
            if i == count:
                total += count
            else:
                break
    count += 1
print total + 2