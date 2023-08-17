import math

def internal_angle_sum(sides):
	return (180*(sides-2), '180*(s-2)')

def internal_angles(sides):
	return (internal_angle_sum(sides)[0]/sides, '180*(s-2)/s')

# given side length and regular polygon
def regular_polygon_area(sides, side_length):
    apothem = side_length/(2*math.tan(math.pi/sides))
    return (sides * side_length * apothem / 2, 's*l*apothem', 'apothem=l/(2*tan(pi/s))')

def print_result(r):
    print('\n'.join(r[1:]))
    input('=' + str(r[0]))

while 1:
    print('1. internal angle sum')
    print('2. internal angles')
    print('3. area')
    mode = input('select mode: ')
    if mode == '1':
        s = int(input('sides: '))
        print_result(internal_angle_sum(s))

    elif mode == '2':
        s = int(input('sides: '))
        print_result(internal_angles(s))

    elif mode == '3':
        s = int(input('sides: '))
        l = float(input('side lengths: '))
        print_result(regular_polygon_area(s, l))
