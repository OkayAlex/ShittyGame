from sys import exit
import random
import RPGClass


Exp = 0

print('''Ты просыпаешься в повозке, в наручниках....
Вокруг тебя несколько пленников. Ты пытаешься объяснить свою невиновность, но тебе никто не верит.
Тебя и других заключенных ведут к плахе...
Имперский офицер проверяет всех по списку..''')

    
def start():
    print('''Выберите свой класс:
Нажмите '1' для воина, '2' для мага, '3' для лучника''')

    character = input("> ")

    if character == "1":
        print("Вы выбрали воина, ваши базовые параметры: \nHP = 3 \nDmg = 1 \nDef = 3 \nExp = 0 ")
    elif character == "2":
        print("Вы выбрали мага, ваши базовые параметры: \nHP = 3 \nDmg = 3 \nDef = 1 \nExp = 0 ")
    elif character == "3":
        print("Вы выбрали лучника, ваши базовые параметры: \nHP = 3 \nDmg = 2 \nDef = 2 \nExp = 0 ")
    else:
        print("Вы ввели неверное число, введите еще раз:")
        start()
        
start()

RPGClass.Castle.enter()
RPGClass.Barracks.enter()
