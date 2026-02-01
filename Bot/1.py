# Изучаю опреаторы if, else,elif

# Сложение 
def addition(x, y):
    return print(x + y)
# Вычитание 
def subtraction(x, y): 
    return print(x - y)
# Деление 
def devision(x, y):               
    return print(x / y)

# Умножение 
def multiplication(x, y): 
    return print(x * y)

number_one = int(input("Напиши первое число" + "\n"))



number_two = int(input("Напиши второе число" + "\n"))



print("Выбери действие")

coice = input("1 - Сложение" + "\n" + "2 - Вычитание" + "\n" + "3 - Деление" + "\n" + "4 - Умножение" + "\n")


if number_two == "0" and coice == "3":
    print("Ошибка, деление на 0 не возможно")

if coice == "1":
    addition(number_one, number_two)
elif coice == "2":
    subtraction(number_one, number_two)
elif coice == "3":
    if number_two == 0:
        print("Ошибка, деление на 0 невозможно")  
    else:
        devision(number_one, number_two)
else: 
    coice == "4"
    multiplication(number_one, number_two)
