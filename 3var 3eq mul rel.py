import math

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

print('--------')
print('a=' + str(a))
print('b=' + str(b))
print('c=' + str(c))