import random
import itertools

CHARACTERS = list("12345678")
LENGTH = 4
MAX_GUESSES = 10

def checkGuess(code, guess):
	paired = zip(code, guess)

	reds = len([i for i, j in paired if i == j])
	whites = sum([min(code.count(i), guess.count(i)) for i in set(code)]) - reds

	return [reds, whites]

def clearTerminal():
	print(chr(27) + "[2J")	# Terminal Escape Sequence to clear terminal

def clearTerminalLine():
	print("\033[A                                                \033[A")

def play():
	win = False
	code = random.choices(CHARACTERS, k=LENGTH)
	guess = None
	guesses = 0

	clearTerminal()
	print("Welcome to Mastermind!")

	while not (win or guesses == MAX_GUESSES):
		guesses += 1
		raw_guess = input("Enter your guess: ").strip()
		if raw_guess == "quit":
			break
		while not (len(raw_guess) == LENGTH):
			clearTerminalLine()
			print(f"Please enter a guess of length {LENGTH}.")
			raw_guess = input("Enter your guess: ")
			clearTerminalLine()
		clearTerminalLine()

		guess = list(raw_guess)
		red, white = checkGuess(code, guess)


		print(f"Enter your guess: {raw_guess}\t\t{red} R \t{white} W \t\t {MAX_GUESSES-guesses} guesses remaining.")

		if red == LENGTH:
			win = True


	print(f"Answer:         : {''.join(code)}")
	if win:
		print("Congratulations! You won!")
	else:
		print("I'm sorry, you lost!")

def bot():
	clearTerminal()

	raw_code = input("Enter your code: ").strip()
	while not (len(raw_code) == LENGTH):
		clearTerminalLine()
		print(f"Please enter a code of length {LENGTH}.")
		raw_code = input("Enter your code: ")
		clearTerminalLine()
	clearTerminalLine()

	code = tuple(raw_code)
	possibilities = list(itertools.product(CHARACTERS, repeat=LENGTH))
	guesses = 0

	while len(possibilities) >= 1:
		guess = random.choice(possibilities)
		guesses += 1
		print(f"{' '.join(guess)}\tPossibilities: {len(possibilities)}\tGuesses: {guesses}")
		result = checkGuess(code, guess)
		print(result)
		if result[0] == LENGTH:
			break
		possibilities.remove(guess)
		possibilities = [possibility for possibility in possibilities if checkGuess(possibility, guess) == result]

	print(f"{' '.join(list(raw_code))}")

def helper():
	clearTerminal()

	possibilities = list(itertools.product(CHARACTERS, repeat=LENGTH))
	guesses = 0

	while len(possibilities) >= 1:
		guess = random.choice(possibilities)
		guesses += 1
		print(f"{' '.join(guess)}\tPossibilities: {len(possibilities)}\tGuesses: {guesses}")

		raw_result = input("Enter your result (R, W): ").strip()
		result = list(map(int, raw_result.split(", ")))
		if result[0] == LENGTH:
			break
		possibilities.remove(guess)
		possibilities = [possibility for possibility in possibilities if checkGuess(possibility, guess) == result]

if __name__ == "__main__":
	helper()
