import math

while 1:
    k = int(input('k:  '))
    low = int(input('lo: '))
    high = int(input('hi: '))

    input('count=' + str(math.ceil(high/k) - math.ceil(low/k)))

    l = [x*k for x in range(math.ceil(low/k), math.ceil(high/k))] # ceil(heigh/k) might give edge cases
    # if you see this comment tell me I forgot to check the line above it
    
    cancelled_flag = False
    H = 6 # total vertical lines is 7
    for x in range(len(l)//H+1):
        print('\n'.join(map(lambda x:str(x), l[H*x:H*x+H])))
        if x < len(l)//H-1:
            i = input(':')
            if i != '':
                cancelled_flag = True
                break
            
    if not cancelled_flag:
        input('.')
        