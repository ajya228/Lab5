#Создайте список из пяти любых чисел. Спросите у пользователя число. Проверьте, есть ли данное число в списке. Выведите исходный список,
# число пользователя и соответствующие сообщение ("Поздравляю, Вы угадали число!" или "Нет такого числа!").

import random
list = [random.sample(range(50), 5)]
number = int(input("Введите число от 1 до 50: "))
if number in list:
   print (f"Список: {list}, Ваше число {number}, Поздравляю, Вы угадали число!")
else: print (f"Список: {list}, Ваше число: {number}, Нет такого числа!")
