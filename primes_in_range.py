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

    print('count=' + str(len(primes)))
    
    H = 6 # total vertical lines is 7
    cancelled_flag = False
    for x in range(len(primes)//H+1):
        print('\n'.join(map(lambda x:str(x), primes[H*x:H*x+H])))
        if x < len(primes)//H-1:
            i = input(':')
            if i != '':
                cancelled_flag = True
                break
            
    if len(primes) % 7 != 0 and not cancelled_flag:
        input('.')