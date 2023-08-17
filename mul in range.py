import math

while 1:
    k = int(input('k:  '))
    low = int(input('lo: '))
    high = int(input('hi: '))

    input('=' + str(math.ceil(high/k) - math.ceil(low/k)))