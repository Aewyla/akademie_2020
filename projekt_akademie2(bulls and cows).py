import random
import time

generated_number = []
def gamenumber():
    global generated_number
    generated_number = random.sample(range(0, 9), 4)
    if generated_number[0] == 0:
        generated_number.clear()
        gamenumber()

gamenumber()
start_time = time.time()
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
    guess_input = input("\nEnter four numbers: ")

    while not guess_input.isdigit():
        print("I said numbers. Try again!")
        guess_input = input("\nEnter four numbers: ")

    while len(guess_input) < 4 or len(guess_input) > 4:
        print("I said 4 numbers. Try again!")
        guess_input = input("\nEnter four numbers: ")

    while len(guess_input) > len(set(guess_input)):
        print("Let's try different numbers, okey? Try, again!")
        guess_input = input("\nEnter four numbers: ")

    guess_list = list(guess_input)
    guess = list(map(int, guess_list))

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


