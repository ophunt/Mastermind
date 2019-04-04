import random, itertools
win, code, guess, guesses = False, random.choices(list("123456"), k=6), None, 0
while not (win or guesses == 10):
	guesses, guess = guesses+1, list(input("Enter your guess: ").strip())
	win, red, white = len([i for i, j in zip(code, guess) if i == j]) == 6, len([i for i, j in zip(code, guess) if i == j]), sum([min(code.count(i), guess.count(i)) for i in set(code)]) - len([i for i, j in zip(code, guess) if i == j])
	print(f"Enter your guess: {''.join(guess)}\t\t{red} R \t{white} W \t\t {10-guesses} guesses remaining.")
print(f"Answer:         : {''.join(code)}\nCongratulations! You won!" if win else f"Answer:         : {''.join(code)}\nI'm sorry, you lost!")
