import math

MAX_ITER = 1000 # 1,000

while 1:
    print('1 ac,bc,ca> a,b,c')
    print('2 a+c,b+c,c+a> a,b,c')
    print('3 c=ka,a:b> min each')
    mode = input('select mode: ')
    if mode == '1':
        ab = float(input('ab='))
        bc = float(input('bc='))
        ac = float(input('ca='))

        '''
        a = ab/b
        c = bc/b
        ab/b * bc/b = ac
        1/b^2 = ac/(ab*bc)
        b = sqrt(ab*bc/ac)
        '''

        b = math.sqrt(ab*bc/ac)
        a = ab/b
        c = bc/b

        print('a=' + str(a))
        print('b=' + str(b))
        input('c=' + str(c))
    
    elif mode == '2':
        a_b = float(input('a+b='))
        b_c = float(input('b+c='))
        c_a = float(input('c+a='))
        
        '''
        (a+b)-(b+c)=a-c
        2c = c+a-(a-c)
        2c = (c+a)-((a+b)-(b+c))
        2c = (c+a)-(a+b)+(b+c)
        c = (c_a-a_b+b_c)/2
        a = c_a-c
        b = b_c-c
        '''
        c = (c_a-a_b+b_c)/2
        a = c_a-c
        b = b_c-c
        
        print('a=' + str(a))
        print('b=' + str(b))
        input('c=' + str(c))
    
    elif mode == '3':
        print('ratio like 5,3')
        c_ka = float(input('c=a*'))
        r_a_b = input('a:b=')
        r_a, r_b = map(int, r_a_b.split(','))
        r_sum = r_a + r_b
        
        '''
        c=c_ka a
        
        a=r_sum/r_a
        b=r_sum/r_b
        [make a,b int]
        '''
        
        a = r_a/r_sum
        b = r_b/r_sum
        
        i = 1
        while ((a*i) % 1 != 0 or (a*i) % 1 != 0 or (a*c_ka*i) % 1 != 0) and i < MAX_ITER:
            i += 1
        
        a = a*i
        b = b*i
        c = a*c_ka # a has already been multiplied by i
        
        if i < MAX_ITER:
            print('a=' + str(a))
            print('b=' + str(b))
            input('c=' + str(c))
        
        else:
            input('unable to solve')