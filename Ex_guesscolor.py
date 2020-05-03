import random
colors=['red','blue','green','black','brown','yellow','white']

while True:
    color=colors[random.randint(0,len(colors)-1)]
    guess=input("I'm thinking about a color,Can you guess it?")

    while True:
        if(color==guess):
            break
        else:
            guess=input('Nope try again!')

    print('you guessed it I was thinking about ',color)

    play_again=input('do you want to play again? type no to quiet')

    if (play_again=='no'):
        break

print('thank you for playing game')
    
