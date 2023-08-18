import math

def prime_factors(n):
    for x in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % x == 0:
            return [x] + prime_factors(n//x)
    
    return [n]

# taken from https://baihuqian.github.io/2018-07-26-factor-combinations/
def factors(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    
    if n == 1:
        return []

    else:
        res = list()
        for f in range(2, int(math.sqrt(n)) + 1):
            if n % f == 0:
                residue = n // f
                res.append([f, residue])
                for l in factors(residue):
                    if l[0] >= f:
                        res.append([f] + l)
        return res

while 1:
    print('1 n> uniq fctr count')
    print('2 n> prime factors')
    print('3 n> unique factors')
    mode = input('select mode: ')
    
    if mode == '1':
        n = int(input('n: '))
        f = factors(n)
        input(len(f))
    
    elif mode == '2':
        n = int(input('n: '))
        p = prime_factors(n)
        input(','.join(map(str, p)))
    
    elif mode == '3':
        n = int(input('n: '))
        f = factors(n)
        H = 6 # total vertical lines is 7
        for x in range(len(f)//H+1):
            print('\n'.join(map(lambda x:str(x), f[H*x:H*x+H])))
            if x < len(f)//H:
                input(':')
                
        if len(f) % 7 != 0:
            input()