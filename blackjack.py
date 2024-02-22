from random import randint

total = 0
LIMIT = 21
banca = 0

def generate_random():
    return randint(1, 14) #generate random number from [1, 13]

def get_value():
    value = generate_random()
    if value == 1:
        total += input(f"Congrats you got a {total}, you get to select the value. Please keep in mind your total is {total}. Will it be 1 or 11?")
    elif total >= 11:
        total += 10

def main():
    total = generate_random()
        
    while True:
        if banca <= 16:
            print(f"My total is {banca}. I must keep getting cards.")
            get_value()
        elif total == 21:
            
            
              
ans = input("Welcome to the blackjack game (simple version)!!. \nDo you know how to play?(y/n)")

main() if ans is "y" else print("REGLAS....")

