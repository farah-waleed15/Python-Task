import random

def nexus_open_door():
    posture=random.choice(['sitting','standing'])
    direction=random.choice(['left','right','facing'])
    distance=random.choice([1,2,3,4,5,6,7,8,9,10])
    print(f'start state -> posture {posture}, direction {direction}, distance {distance}')

    if posture=='sitting':
        print('nexus stands up')
    elif posture=='standing':
        print('do nothing')

    if direction=='left' or 'right':
        print('nexus turns towards the door')
    elif direction=='facing':
        print('do nothing')

    while distance>0:
        print(f'moving... {distance} steps left')
        distance=distance-1

print(nexus_open_door())


