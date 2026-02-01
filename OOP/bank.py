class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self._account_number = account_number
        self._holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print(f'Ваш баланс пополнен на {amount} рублей, баланс: {self.__balance}')
        
        else:
            print('Ошибка пополнения')


    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance =  self.__balance - amount
            print(f'Вы успешно сняли {amount} рублей, баланс: {self.__balance}')

    def get_balance(self):
        print(f'Ваш счет: {self.__balance} рублей')
        return self.__balance
    
    def display_info(self):
        print(f'Номер счета: {self._account_number}.')
        print(f'Имя владельца счета: {self._holder_name}.')
        print(f'Баланс {self.__balance} рублей.')

account = BankAccount('123456', 'Иванов Иван', 1000)

# Тестируем все методы
print("=== Начальное состояние ===")
account.display_info()

print("=== После операций ===")
account.deposit(600)
account.withdraw(100)
account.get_balance()
account.display_info()