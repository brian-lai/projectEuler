def isPalin(product):
    string = str(product)
    length = len(string) - 1
    palinCheck = ''
    while length >= 0:
        palinCheck += string[length]
        length-=1
        
    return (palinCheck == string)

    
        
    
largestPalindrome = 0

for i in range(100,1000):
    for j in range(100,1000):
        product = i*j
        if product > largestPalindrome and isPalin(product):
            largestPalindrome = product

print largestPalindrome

