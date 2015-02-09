first = 1
second = 2
third = 0
total = 0

while third < 4000000:
    if third%2 == 0:
        total += third
        print third
    third = first + second
    first = second
    second = third
print total + 2