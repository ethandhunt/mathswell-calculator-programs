import math

while 1:
    k = int(input('k:  '))
    low = int(input('lo: '))
    high = int(input('hi: '))

    for x in range(math.ceil(low/k), math.ceil(high/k)):
        print(k*x)
        
    input('=' + str(math.ceil(high/k) - math.ceil(low/k)))