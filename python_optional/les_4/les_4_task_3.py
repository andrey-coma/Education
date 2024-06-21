'''
У вас есть банковская карта с начальным балансом равным 0 у.е.
Вы хотите управлять этой картой, выполняя следующие операции,
для выполнения которых необходимо написать следующие функции:

check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
deposit(amount): Пополнение счёта.
withdraw(amount): Снятие денег.
exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.

Пополнение счета:

Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму.
Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.

Снятие средств:

Функция withdraw(amount) позволяет клиенту снимать средства со счета.
Сумма снятия также должна быть кратной MULTIPLICITY.
При снятии средств начисляется комиссия в процентах от снимаемой суммы,
которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.

Завершение работы:

Функция exit() завершает работу с банковским счетом.
Перед завершением, если на счету больше RICHNESS_SUM,
начисляется налог на богатство в размере RICHNESS_PERCENT процентов.

Проверка кратности суммы:

Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY.
Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.
'''

import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


def check_multiplicity(amount):
    """
    Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY.
    Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.
    """
    if not amount % MULTIPLICITY == 0:
        return False

    return True


def deposit(amount):
    """
    Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму.
    Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.
    """
    global bank_account

    if check_multiplicity(amount):
        bank_account += amount
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
        return bank_account

    print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')


def withdraw(amount):
    """
    Функция withdraw(amount) позволяет клиенту снимать средства со счета.
    Сумма снятия также должна быть кратной MULTIPLICITY.
    При снятии средств начисляется комиссия в процентах от снимаемой суммы,
    которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.
    """
    global bank_account

    percent = PERCENT_REMOVAL * amount

    if percent < MIN_REMOVAL:
        percent = MIN_REMOVAL

    elif percent > MAX_REMOVAL:
        percent = MAX_REMOVAL

    if bank_account < amount + percent:
        operations.append(
            f'Недостаточно средств. Сумма с комиссией {int(percent + amount)} у.е. На карте {bank_account} у.е.')

    if not check_multiplicity(amount):
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')

    if check_multiplicity(amount) and (bank_account > amount + percent):
        bank_account -= amount
        bank_account -= percent
        operations.append(
            f'Снятие с карты {amount} у.е. Процент за снятие {int(percent)} у.е.. Итого {int(bank_account)} у.е.')


def exit():
    """
    Функция exit() завершает работу с банковским счетом.
    Перед завершением, если на счету больше RICHNESS_SUM,
    начисляется налог на богатство в размере RICHNESS_PERCENT процентов.
    """
    global bank_account

    if bank_account > RICHNESS_SUM:
        percent_rich = bank_account * RICHNESS_PERCENT
        bank_account -= percent_rich
        operations.append(f'Вычтен налог на богатство 0.1% в сумме {percent_rich} у.е. Итого {bank_account} у.е.')

    operations.append(f'Возьмите карту на которой {bank_account} у.е.')


deposit(1000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()


print(operations)