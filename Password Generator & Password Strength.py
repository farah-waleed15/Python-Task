import random
import string

choice=input('choose an option:\n1.generate a random password\n2.evaluate password strength\nenter choice (1 or 2): ')
if choice=='1':
    while True:
        length=int(input('enter password length (minimum 8): '))
        if length<8:
            print('password length must be at least 8 characters.')
            continue
        upper=string.ascii_uppercase
        lower=string.ascii_lowercase
        digits=string.digits
        symbols='!@#$%&*?_'
        characters=upper+lower+digits+symbols
        password=[random.choice(upper), random.choice(lower), random.choice(digits), random.choice(symbols)]
        for _ in range(length-4):
            password.append(random.choice(characters))
        random.shuffle(password)
        final_password=''.join(password)
        print('generated password:\n')
        print(final_password)
        satisfaction=input('are you satisfied with this password? (y/n): ')
        if satisfaction=='y':
            break

elif choice=='2':
    password=input('enter your password: ')
    length=len(password)>=8
    lower=any(c.islower() for c in password)
    upper=any(c.isupper() for c in password)
    digit=any(c.isdigit() for c in password)
    symbol=any(c in '!@#$%&*?_' for c in password)
    requirements=[length, lower, upper, digit, symbol]
    failed_count=requirements.count(False)
    if failed_count>=3:
        strength='weak'
    elif failed_count==2:
        strength='medium'
    elif failed_count==1:
        strength='strong'
    else:
        strength=' strong'
    print(f'password strength: {strength}')

    if strength in ['weak','medium']:
        print('suggestions for improvement:\n')
        if not length:
            print('- increase the length to at least 8 characters')
        if not lower:
            print('- add lowercase letter')
        if not upper:
            print('- add uppercase letter')
        if not digit:
            print('- add numbers')
        if not symbol:
            print('- add special characters')

