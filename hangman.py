import random

word_bank = [
    "fish",
    "computer",
    "chair",
    "television",
    "dog",
    "animal",
    "tree",
    "bag",
    "towel",
    "battery",
    "happy",
]


STEPS = 7
current = []
letter_bank = set() #set para no repetir letras

def draw():
    print("Here comes a draw...")

def update_draw():
    print("Here should be the draw updated...")

def write_letter(pal, guess):
    for i in pal:
        if i == guess:
            current[pal.index(i)] = guess
    letter_bank.add(guess)
        

def write_empty(n):
    for i in range(n):
        current.append("_")


def ingame(word):
    i = 0
    while i < STEPS + 1:
        print(current)
        guess = input()
        if len(guess) == 1 and guess.isalpha():
            if guess in word:
                if guess in letter_bank:
                    print(f"You've already said that. {STEPS - i} opportunities remaining.")
                else:
                    print(f"That's correct!! {STEPS - i} opportunities remaining.")
                    write_letter(word, guess)
                    draw()
            else:
                if guess in letter_bank:
                    print(f"You've already said that. {STEPS - i} opportunities remaining.")
                else:
                    update_draw()
                    draw()
                    letter_bank.add(guess)
                    if STEPS - i == 0:
                        print(f"You've run out of guesses. The secret word was {word.upper()}.")
                        exit()
                    i += 1
                    print(f"{guess} is not on the secret word. {STEPS - i} opportunities remaining.")
        elif guess.isalpha():
            if guess == word:
                print(f"Congrats!! You've discovered the secret word: {word.upper()}")
                exit()
            else:
                update_draw()
                draw()
                if STEPS - i == 0:
                    print(f"You've run out of guesses. The secret word was {word.upper()}.")
                    exit()
                i += 1
                print(f"{guess} is not the secret word. {STEPS - i} opportunities remaining.")
        else:
            print("You must select a letter or a word.")
            
            
        if "_" in current:
            print("LETTERS SAID:", letter_bank)
        else:
            print("Congrats!! You've discovered the secret word.")
            print(current)
            exit()


def main():
    name = input("Welcome to the hangman game!!! What is your name? ")
    print(f"Nice to meet you {name}!")
    while True:
        option = input("Are you ready to play? (y/n) ")
        if option == "y":
            break
        elif option == "n":
            print("Oh, I'm so sad you don't wanna play :(")
            exit()
        else:
            print("Please enter a valid answer, y for yes or n for not.")
    print("Lets start the game!!!")

    num = random.randint(0, len(word_bank) - 1)
    word = word_bank[num]
    write_empty(len(word))
    ingame(word)


main()