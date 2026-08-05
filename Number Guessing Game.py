import random

print('welcome player\n')
print("I'm thiking of a number between 1 and 100.\n")
print('you have 6 attempts to guess it\n')

rounds_played=0
rounds_won=0
total_score=0
play_again='y'

while play_again == 'y':
    secret_number=random.randint(1,100)
    attempts=6
    guessed_correctly=False
    rounds_played += 1

    for attempt in range(1,attempts+1):
        print(f'attempt {attempt}/6')
        guess=int(input('enter your guess:'))
        diff=guess-secret_number
        if diff==0:
            print('congratulations!\n')
            print('you guessed the number\n')
            guess_remaining=attempts-attempt
            print(f'guess remaining: {guess_remaining}\n')
            multiplier=guess_remaining+1
            print(f'multiplier: ×{multiplier}\n')
            points_earned=guess_remaining +1
            print(f'points earned: {points_earned}\n')
            total_score+=points_earned
            print(f'current score: {total_score}\n')
            rounds_won+=1
            guessed_correctly=True
            break
        elif diff<-10:
            print('too low\n')
        elif diff>10:
            print('too high\n')
        elif diff<0:
            print('higher\n')
        else:
            print('lower\n')
    if not guessed_correctly:
        print(f'out of attempts! the secret number was {secret_number}\n')
    play_again=input(f'play another round? (y/n): \n')

print(f'rounds played: {rounds_played}\n')
print(f'rounds won: {rounds_won}\n')
print(f'final score: {total_score}\n')
