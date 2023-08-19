while 1:
    print('1 o,v,a,A> next value')
    print('2 o,v,a,V> next avg')
    mode = input('select mode: ')
    
    if mode == '1':
        o = float(input('Original avg: '))
        v = float(input('Previous value: '))
        a = float(input('Resulting avg: '))
        if o-a == 0:
            print('o-a=0 is unconstrained')
            print('k=(a-s)/(o-a)')
            input('div by 0')
            continue
        
        A = float(input('Next avg:'))
        
        '''
        n/k = o
        (n+v)/(k+1) = a
        n+v=ak+a
        n-ak=a-v
        n/k-a=(a-v)/k
        o-a=(a-v)/k
        k(o-a)=a-v
        
        k=(a-v)/(o-a)
        n=ko
        
        (n+v+V)/(k+2)=A
        V=kA+2A-n-v
        '''
        
        k = (a-v)/(o-a)
        n = k * o

        V = k*A + 2*A - n - v
        input('V=' + str(v))
    
    if mode == '2':
        o = float(input('Original avg: '))
        v = float(input('Previous value: '))
        a = float(input('Resulting avg: '))
        if o-a == 0:
            print('o-a=0 is unconstrained')
            print('k=(a-v)/(o-a)')
            input('div by 0')
            continue

        V = float(input('New value: '))
        
        '''
        k=(a-v)/(o-a)
        n=ko
        
        (n+v+V)/(k+2)=A
        '''
        
        k = (a-v)/(o-a)
        n = k*o
        
        A = (n+v+V)/(k+2)
        input ('A=' + str(A))