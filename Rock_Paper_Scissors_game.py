import random

rps = ['rock', 'paper', 'scissors']
answer = input('Rock Paper Scissors ? ')
answer = answer.lower()

def rpsgame(a):
    if random.choice(rps) == a:
        print('Draw')
    elif random.choice(rps) == 'rock' and a == 'paper':
        print('You win')
    elif random.choice(rps) == 'scissors' and a == 'rock':
        print('You win')
    elif random.choice(rps) == 'paper' and a == 'scissors':
        print('You win')
    else:
        print('You lost')
rpsgame(answer)