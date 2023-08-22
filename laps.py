import math

# assume fastest as datum
def overtake_time_by_lap_times(A_lap_time, B_lap_time, overtakes):
    '''
    A_laps = t/A_lap_time
    B_laps = t/B_lap_time
    
    A_laps = B_laps + overtakes
    
    t/A_lap_time = t/B_lap_time + overtakes
    B_lap_time t = A_lap_time t + A_lap_time B_lap_time overtakes
    t = A_lap_time B_lap_time overtakes / (B_lap_time - A_lap_time)
    '''
    
    return (A_lap_time * B_lap_time * overtakes / (B_lap_time - A_lap_time))

def overtake_lap_by_lap_times(A_lap_time, B_lap_time, overtakes):
    return math.ceil(overtake_time_by_lap_times(A_lap_time, B_lap_time, overtakes)/A_lap_time)

def overtake_time_by_lap_times_offset(A_lap_time, B_lap_time, offset_time, overtakes):
    '''
    A_laps = t/A_lap_time
    B_laps = (t+offset)/B_lap_time
    
    A_laps = B_laps + overtakes
    
    t/A_lap_time = (t+offset)/B_lap_time + overtakes
    B_lap_time t = A_lap_time t + A_lap_time offset + A_lap_time B_lap_time overtakes
    t = (A_lap_time offset + A_lap_time B_lap_time overtakes) / (B_lap_time - A_lap_time)
    '''
    
    return (A_lap_time * offset_time + A_lap_time * B_lap_time * overtakes) / (B_lap_time - A_lap_time)

def overtake_time_by_speed_lap_length_offset(A_speed, B_speed, lap_length, offset_dist, overtakes):
    '''
    A_laps = (t A_speed) / lap_length
    B_laps = (t B_speed + offset) / lap_length
    
    A_laps = B_laps + overtakes
    
    ta/L = (tb+O)/L + o
    at = bt+O+oL
    at-bt = O+oL
    t(a-b) = O+oL
    t = (O+oL)/(a-b)
    '''
    
    return (offset_dist + overtakes * lap_length) / (A_speed - B_speed)

while 1:
    print('1 A,B,o> ovrtk time')
    print('2 A,B,o> ovrtk lap(A)')
    print('3 A,B,O,o> time')
    print('4 a,b,L,O,o> time')
    
    mode = input('select mode: ')
    
    if mode == '1':
        A = float(input('A lap time: '))
        B = float(input('B lap time: '))
        if B-A == 0:
            print('B-A=0 is unconstrained')
            print('ABo/(B-A)')
            input('div by 0')
            continue

        o = float(input('Overtakes: '))
        print('ABo/(B-A)')
        input('t=' + str(overtake_time_by_lap_times(A, B, o)))
    
    if mode == '2':
        A = float(input('A lap time: '))
        B = float(input('B lap time: '))
        if A-B == 0:
            print('A-B=0 is unconstrained')
            print('ceil(Bo/(A-B))')
            input('div by 0')
            continue
        
        o = float(input('Overtakes: '))
        print('ceil(Bo/(A-B))')
        print('in A laps,')
        input('l=' + str(overtake_lap_by_lap_times(A, B, o)))
    
    if mode == '3':
        A = float(input('A lap time: '))
        B = float(input('B lap time: '))
        if B-A == 0:
            print('B-A=0 is unconstrained')
            print('t=(AO+ABo)/(B-A)')
            input('div by 0')
            continue

        O = float(input('Time offset: '))
        o = float(input('Overtakes: '))
        input('t=' + overtake_time_by_lap_times_offset(A, B, O, o))
        
    if mode == '4':
        a = float(input('A speed: '))
        b = float(input('B speed: '))
        if b-a == 0:
            print('b-a=0 is unconstrained')
            print('t=(aO+abo)/(bL-aL)')
            input('div by 0')
            continue
        
        L = float(input('Lap length: '))
        if L == 0:
            print('L=0 is unconstrained')
            print('t=(aO+abo)/(bL-aL)')
            input('div by 0')
            continue
        
        O = float(input('Offset dist: '))
        o = float(input('Overtakes: '))
        input('t=' + str(overtake_time_by_speed_lap_length_offset(a, b, L, O, o)))