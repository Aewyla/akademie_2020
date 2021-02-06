import random
import time

start_time = time.time()
generated_number = random.sample(range(0, 9), 4)
cows = 0
bulls = 0
score = 0

print('''
Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
''')

while bulls < 4:
    cows = 0
    bulls = 0

    guess_input = list(input("\nEnter four numbers: "))
    guess = list(map(int, guess_input))

    while len(guess) < 4 or len(guess) > 4:
        print("That guess is invalid!")
        guess_input = list(input("\nEnter four numbers: "))
        guess = list(map(int, guess_input))


    for i in range(len(generated_number)):
        if guess[i] in generated_number and guess[i] != generated_number[i]:
            cows += 1
        if guess[i] in generated_number and guess[i] == generated_number[i]:
            bulls += 1

    print("Cows:  ", cows)
    print("Bulls: ", bulls)
    score += 1

elapsed_time = time.time() - start_time

print("Correct, you've guessed the right number in", score, "guesses!")
print('Your time:', (time.strftime("%H:%M:%S", time.gmtime(elapsed_time))))


