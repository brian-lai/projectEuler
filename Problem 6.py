sumSquare = 0
squareSum = 0

for i in range(1,101):
    sumSquare += i**2
    squareSum += i

diff = squareSum**2 - sumSquare
print diff