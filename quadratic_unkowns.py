while 1:
    print('1 x,a,B,C> K')
    print('2 x,b,A,C> K')
    print('3 x,c,A,B> K')
    mode = input('select mode: ')
    
    if mode == '1':
        print('ax^2 + BKx + CK = 0')
        x = float(input('x='))
        if x == 0:
            print('x=0 is unconstrained')
            input('no k in 0+CK=0')
            continue

        a = float(input('a='))
        if a == 0:
            input('a=0 is invalid')
            continue
        
        B = float(input('B='))
        C = float(input('C='))
        if B*x + C == 0:
            print('Bx+C=0 unconstrained') # not enough space for 'is'
            print('K=ax^2/(Bx+C)')
            input('div by 0')
            continue
        
        '''
        ax^2+BKx+CK=0
        K(Bx+C)=ax^2
        K=ax^2/(Bx+C)
        '''
        
        K = a*x**2/(B*x+C)
        
        if a*x**2 + B*K*x + C*K != 0: # idk if this ever happens
            print('invalid solution')
            print('ax^2+BKx+CK!=0')
        
        input('K=' + str(K))

    elif mode == '2':
        print('AKx^2 + bx + CK = 0')
        x = float(input('x='))
        if x == 0:
            print('x=0 is unconstrained')
            input('no K in 0+CK=0')
            continue
            
        A = float(input('A='))
        if A == 0:
            input('A=0 is invalid')
            continue
            
        b = float(input('b='))
        C = float(input('C='))
        if A*x**2 + C == 0:
            print('Ax^2+c=0 unconstrained') # not enough space for 'is' (or -'ed')
            print('K=bx/(Ax^2+C)')
            input('div by 0')
            continue
        
        '''
        AKx^2+bx+CK=0
        AKx^2+CK=bx
        K(Ax^2+C)=bx
        K=bx/(Ax^2+C)
        '''
        
        K = b*x/(A*x**2+C)

        if a*x**2 + B*K*x + C*K != 0: # idk if this ever happens
            print('invalid solution')
            print('ax^2 + BKx + CK != 0')

        input('K=' + str(K))
    
    elif mode == '3':
        print('AKx^2 + BKx + c = 0')
        x = float(input('x='))
        if x == 0:
            print('x=0 is unconstrained')
            input('no K in 0+c=0')
            continue

        A = float(input('A='))
        if A == 0:
            input('A=0 is invalid')
            continue

        B = float(input('B='))
        if A*x**2+B*x == 0:
            print('Ax^2+Bx=0 unconstrained')
            print('K=c/(Ax^2+Bx)')
            input('div by 0')
            continue
        
        c = float(input('c='))
        
        '''
        AKx^2+BKx+c=0
        K(Ax^2+Bx)=c
        K=c/(Ax^2+Bx)
        '''
        
        K = c/(A*x**2+B*x)

        if a*x**2 + B*K*x + C*K != 0: # idk if this ever happens
            print('invalid solution')
            print('ax^2 + BKx + CK != 0')

        input('K=')