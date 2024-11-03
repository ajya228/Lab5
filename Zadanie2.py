#Создайте любой список. Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран это значение.
import random
list = [random.randint(1, 10) for _ in range(10)]
dub = []
count = 0
for i in range (10):
    if list.count(i) > 1 and i not in dub:
        count += list.count(i)
        dub.append(i)
print (f"Список: {list}, Повторяющиеся элементы: {dub}, Общее число повторений встречающихся в списке: {count}")