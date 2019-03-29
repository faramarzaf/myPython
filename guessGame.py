import random
result = random.randint(1,99)
name = input('whats is your name? ')
guess = input('whats is your guess? ')
guess = int(guess)

while guess != result:
    if guess > result:
        print ("Mine is smaller!")
    else:
        print ("Mine is larger!")
    guess = input('whats is your guess? ')
    guess = int(guess)

print("woooow!!",name, "you did it!")