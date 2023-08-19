import math

def internal_angle_sum(sides):
	return (180*(sides-2), '180*(s-2)')

def internal_angles(sides):
	return (internal_angle_sum(sides)[0]/sides, '180*(s-2)/s')

# given side length and regular polygon
def regular_polygon_area(sides, side_length):
    apothem = side_length/(2*math.tan(math.pi/sides))
    return (sides * side_length * apothem / 2, 's l apothem', 'apothem=l/(2tan(pi/s))')

def polygon_side_from_radius(sides, radius):
    return (2 * radius * math.sin(math.pi/sides), '2r sin(pi/s)')

def polygon_side_from_apothem(sides, apothem):
    return (2 * apothem * math.tan(math.pi/sides), '2 apothem tan(pi/s)')

def apothem_from_sides_side_length(sides, side_length):
    return (side_length/(2*math.tan(math.pi/sides)), 'l/(2tan(pi/s))')

def apothem_from_sides_outcircle(sides, circumradius):
    return (circumradius*math.cos(math.pi/sides), 'R cos(pi/s)')

def print_result(r):
    print('\n'.join(r[1:]))
    input('=' + str(r[0]))

while 1:
    print('1 s> intr angle sum')
    print('2 s> intr angles')
    print('3 s,l> area')
    print('4 s,r> side length')
    print('5 s,a> side length')
    print('6 s,l> apothem')
    mode = input('mode (more): ')
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
    
    elif mode == '4':
        s = int(input('sides: '))
        r = float(input('radius: '))
        print_result(polygon_side_from_radius(s, r))
    
    elif mode == '5':
        s = int(input('sides: '))
        a = float(input('apothem: '))
        print_result(polygon_side_from_apothem(s, a))
        
    elif mode == '6':
        s = int(input('Sides: '))
        l = float(input('Side length: '))
        print_result(apothem_from_sides_side_length(s, l))
    
    elif mode == '':
        print('7 s,R> apothem')
        mode = input('select mode: ')
        if mode == '7':
            s = int(input('Sides: '))
            R = float(input('Circumradius: '))
            print_result(apothem_from_sides_outcircle(s, R))
        
        else:
            print('invalid mode')
        

    else:
        print('invalid mode')