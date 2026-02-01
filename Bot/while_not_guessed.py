    # Угадай число игра

from tkinter import *
import random


secret_number = random.randint(1, 100)

attempts = 0
guessed = False




def check_result():
    global attempts
    guess = entry.get()

    try:
        guess_number = int(guess)
        attempts = attempts + 1

        if guess_number == secret_number:
            label.config(text=f'Вы угадали, правильное число {guess_number} \n за {attempts} попыток!')
        elif guess_number < secret_number:
            label.config(text=f'Введенное вами число меньше загаданного')
        else:
            label.config(text =f'Введенное вами число больше загаданного')
    
    except:
        label.config(text='Ошибка, введите число!')    
    entry.delete(0, END)

window = Tk()
window.title('Игра угадай число')
window.geometry('450x200')
label = Label(window, text='Введи число от 1 до 100', font=("Verdana", 13))
entry = Entry(window, width=5, font=("Verdana", 15))
label.pack(pady=15)
entry.pack(pady=10)
button = Button(window, text='Проверить', command=check_result, font=("Verdana", 12))
button.pack(pady=10)
window.config(bg='lightblue')
label.config(bg='lightblue')
button.config(bg='#f0f8ff')
entry.config(bg='#f0f8ff')
window.mainloop()
