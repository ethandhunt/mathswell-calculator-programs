import math

k = int(input('k:  '))
low = int(input('lo: '))
high = int(input('hi: '))

print('=' + str(math.ceil(high/k) - math.ceil(low/k)))