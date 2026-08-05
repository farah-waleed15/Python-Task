import time

minutes = int(input('enter the minutes for the test: '))
seconds = int(input('enter the seconds for the test: '))
total_seconds = (minutes*60) + seconds

if total_seconds<=0 or seconds>59:
    print('Invalid test duration')
    exit()

if total_seconds>300:
    print('Safety limit exceeded! Test duration capped to 5:00.')
    total_seconds = 300

while total_seconds>=0:
    mins=total_seconds//60
    secs=total_seconds%60
    time_convert=f'{mins:02d}:{secs:02d}'

    if total_seconds>30:
        status=f'POWER ON | time remaining: {time_convert}'
    elif total_seconds>10:
        status=f'STABILIZING SYSTEM | time remaining: {time_convert}'
    elif total_seconds>0:
        status=f'COOLDOWN PHASE | Do not touch | {time_convert}'
    else:
        print('power test completed successfully \n')
        break

    print(f'{status}\n')
    total_seconds -=1

print()


