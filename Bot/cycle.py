            ### игра угадай число ###

import random

secret_number = random.randint(1, 100)

attemps = 0
guessed = False


while not guessed:
    guess = int(input('Введите число от 1 до 100: '))
    attemps += 1

    if guess == secret_number:
        print('Поздраляю, ты угадал загаданное число!')
        guessed = True

    elif guess < secret_number:
        print('Загаданное число больше')
    else:
        print('Загаданное число меньше')