import math

while 1:
    lo = int(input('lo: '))
    hi = int(input('hi: '))

    count = 0
    primes = []
    for x in range(lo, hi+1):
        div_flag = False
        for y in range(2, math.ceil(math.sqrt(x))):
            if x%y == 0:
                div_flag = True
                break
        
        if not div_flag:
            count += 1
            primes.append(str(x)) # str conversion here

    print('\n'.join(primes))
    input('=' + str(count))