number=7
guess=int(input('guess a number between 1 to 10:'))

while True:
    if guess==number:
        break
    else:
       guess=int(input('Nop,try again'))
print('Yes the number is',number)

