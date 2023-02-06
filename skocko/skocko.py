import random

symbols = ['t', 'c', 'p', 'h', 's', 'z']
guessed = False
end = False

def generate_combination():
    symbol1 = random.choice(symbols)
    symbol2 = random.choice(symbols)
    symbol3 = random.choice(symbols)
    symbol4 = random.choice(symbols)

    combination = [symbol1, symbol2, symbol3, symbol4]
    return combination

def read_guess():
    guess = input()
    guess_list = guess.split(" ")
    print(guess_list)
    return guess_list

def check_guess(guess):
    global guessed

    good_spot_counter = 0
    good_symbol_counter = 0
    temp = zip(guess, combination)
    to_remove = []
    counter = 0
    for x, y in temp:
        if x == y:
            to_remove.append(counter)
            good_spot_counter += 1
        counter += 1
    
    to_remove.reverse()
    for position in to_remove:
        del guess[position]
        del combination[position]

    for char in guess:
        for symbol in combination:
            if char == symbol:
                combination.remove(symbol)
                good_symbol_counter += 1
                break
    
    print("GOOD SPOTS: ", good_spot_counter)
    print("GOOD SYMBOLS: ", good_symbol_counter)

    if good_spot_counter == 4:
        guessed = True

combination = generate_combination()

temp_combination = combination.copy()

try_conter = 0
while(not guessed and not end):
    combination = temp_combination.copy()
    guess = read_guess()
    check_guess(guess)
    try_conter += 1
    if try_conter == 6:
        end = True
