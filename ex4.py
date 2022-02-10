# Заполните 2 списка а и b случайными целыми числами и верните 3 список общих для а и b элементов
import random

list_1 = [random.randint(1,10) for i in range(10)]
list_2 = [random.randint(1,10) for i in range(10)]

def number(list_1, list_2):
    print(f"{list_1}\n{list_2}")
    return [i for i in list_1 if i in list_2]

print(number(list_1,list_2))