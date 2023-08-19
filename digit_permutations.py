def var_permutations(var):
    # var as [(B,1), (A,2)]
    result = []
    for x in range(10):
        if len(var) > 1:
            for y in var_permutations(var[1:]):
                result.append(x*10**var[0][1]+y)
                
        else:
            result.append(x*10**var[0][1])
    return result


def permutations(n_input):
    n_constant = 0
    n_var = [] # [(B, 1), (A, 2)]
    i = len(n_input)
    for x in n_input:
        i -= 1
        if x.isdigit():
            n_constant += int(x) * 10**i
        
        else:
            n_var.append((x, i))

    result = []
    for x in var_permutations(n_var):
        result.append(n_constant+x)
    
    return result


while 1:
    print('1 k,n> count')
    print('2 k,n> list')
    mode = input('select mode: ')
    
    if mode == '1':
        print('all 12ab5 div by k')
        k = int(input('Divisor: '))
        n_input = input('N: ')
        
        c = 0
        for x in permutations(n_input):
            if x%k == 0:
                c += 1

        input('c=' + str(c))
    
    if mode == '2':
        print('all 12ab5 div by k')
        k = int(input('Divisor: '))
        n_input = input('N: ')
        
        n_permutations = [x for x in permutations(n_input) if x % k == 0]
        H = 7
        cancelled_flag = False
        for x in range(len(n_permutations)//H+1):
            print('\n'.join(map(lambda x:str(x), n_permutations[H*x:H*x+H])))
            if x < len(n_permutations)//H-1:
                i = input(':')
                if i != '':
                    cancelled_flag = True
                    break
                
        if len(n_permutations) % 7 != 0 and not cancelled_flag:
            input('.')