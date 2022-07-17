from random import randint
import random as r





class Player(object):
    hp = 10
    max_hp = 10
    atk = 2
    lvl = 0
    sp = 1 #skill point
    exp = 0
    max_exp = 100
    heal = 3


print("Вы входите в магический куб рандома. Приготовтесь к испытаниям.")


def upgrade(Player):
    while Player.sp > 0:
        print("Доступны очки навыков. Кол-во очков {}".format(Player.sp))
        print("Нажмите 1, чтобы повысить HP на 5")
        print("Нажмите 2, чтобы повысить атаку на 1")
        print("Нажмите 3, чтобы повысить исцеление на 2")
        n = input("> ")
        if n == "1":
            Player.hp += 5
            Player.sp -= 1
            Player.max_hp += 5
        if n == "2":
            Player.atk += 2
            Player.sp -= 1
        if n == "3":
            Player.heal += 1
            Player.sp -= 1


def stats(Player):
    print("Ваши текущие характеристики:")
    print("HP: {}/{}".format(Player.hp, Player.max_hp))
    print("Атака: {}".format(Player.atk))
    print("Исцеление: {}".format(Player.heal))
    print("Опыт: {}/{}".format(Player.exp, Player.max_exp))
    print("Уровень: {}".format(Player.lvl))
    input("Enter чтобы продолжить")


def random_event(Player):
    while True:
        print("Что делаем?")
        print("Нажми 1, чтобы пойти сражаться")
        print("Нажми 2, чтобы проверить свои характеристики")
        n = input("> ")
        if n == "1":
            random_battle(Player)
        if n == "2":
            stats(Player)
      

def random_battle(Player):
    enemy = r.randint (1,3)
    if enemy == 1:
        ork(Player)
    if enemy == 2:
        dragon(Player)
    if enemy == 3:
        boss(Player)
    


def ork(Player):
    enemy_hp = 2
    enemy_atk = 1
    print("Вы встретили орка.")
    print("Его HP: {}".format(enemy_hp))
    print("Его атака:{}".format(enemy_atk))
    
    while enemy_hp > 0:
        print("Нажмите 1, чтобы атаковать")
        print("Нажмите 2, чтобы вылечиться (+{})". format(Player.heal))
        print("Нажмите 3, чтобы убежать")
        n = input("> ")
        if n == "1":
            enemy_hp -= Player.atk
            print("Вы нанесли урон {}".format(Player.atk))
            Player.hp -= enemy_atk
            print("Вам нанесли урон: {}". format(enemy_atk))
            if Player.hp < 0:
                print("Вы проиграли...")
                random_event(Player)
        if n == "2":
            Player.hp -= enemy_atk
            print("Вам нанесли урон: {}". format(enemy_atk))
            Player.hp += Player.heal
            if Player.hp <= 0:
                Player.hp = 0
            print("Вы восстановили здоровье  (+{})".format(Player.heal))
            if Player.hp > Player.max_hp:
                Player.hp = Player.max_hp
            print("Текущее здоровье: {}".format(Player.hp))
            if Player.hp < 0:
                print("Вы проиграли...")
                random_event(Player)
            
        if n == "3":
            x = r.randint(1, 3)
            if x == "2":
                print("Вам удается убежать!")
                random_event(Player)
            else:
                print("Вам не удается сбежать")
        
        if enemy_hp <= 0:
            print("Вы победили, получите + 1 опыт")
            Player.exp += 1
            if Player.exp >= Player.max_exp:
                Player.exp = 0
                Player.max_exp *= 5
                Player.lvl += 1
                upgrade(Player)       
            print("Текущий опыт: {} ".format(Player.exp))


def dragon(Player):
    enemy_hp = 4
    enemy_atk = 2
    print("Вы встретили дракона.")
    print("Его HP: {}".format(enemy_hp))
    print("Его атака:{}".format(enemy_atk))
    
    while enemy_hp > 0:
        print("Нажмите 1, чтобы атаковать")
        print("Нажмите 2, чтобы вылечиться (+{})". format(Player.heal))
        print("Нажмите 3, чтобы убежать")
        n = input("> ")
        if n == "1":
            enemy_hp -= Player.atk
            print("Вы нанесли урон {}".format(Player.atk))
            Player.hp -= enemy_atk
            print("Вам нанесли урон: {}". format(enemy_atk))
            if Player.hp < 0:
                print("Вы проиграли...")
                random_event(Player)
        if n == "2":
            Player.hp -= enemy_atk
            print("Вам нанесли урон: {}". format(enemy_atk))
            Player.hp += Player.heal
            if Player.hp <= 0:
                Player.hp = 0
            print("Вы восстановили здоровье  (+{})".format(Player.heal))
            if Player.hp > Player.max_hp:
                Player.hp = Player.max_hp
            print("Текущее здоровье: {}".format(Player.hp))
            if Player.hp < 0:
                print("Вы проиграли...")
                random_event(Player)
            
        if n == "3":
            x = r.randint(1, 3)
            if x == "2":
                print("Вам удается убежать!")
                random_event(Player)
            else:
                print("Вам не удается сбежать")
        
        if enemy_hp <= 0:
            print("Вы победили, получите + 10 опыта")
            Player.exp += 10
            if Player.exp >= Player.max_exp:
                Player.exp = 0
                Player.max_exp *= 5
                Player.lvl += 1
                upgrade(Player)       
            print("Текущий опыт: {} ".format(Player.exp))

def boss(Player):
    enemy_hp = 6
    enemy_atk = 3
    print("Вы встретили древнее чудовище.")
    print("Его HP: {}".format(enemy_hp))
    print("Его атака:{}".format(enemy_atk))
    
    while enemy_hp > 0:
        print("Нажмите 1, чтобы атаковать")
        print("Нажмите 2, чтобы вылечиться (+{})". format(Player.heal))
        print("Нажмите 3, чтобы убежать")
        n = input("> ")
        if n == "1":
            enemy_hp -= Player.atk
            print("Вы нанесли урон {}".format(Player.atk))
            Player.hp -= enemy_atk
            print("Вам нанесли урон: {}". format(enemy_atk))
            if Player.hp < 0:
                print("Вы проиграли...")
                random_event(Player)
        if n == "2":
            Player.hp -= enemy_atk
            print("Вам нанесли урон: {}". format(enemy_atk))
            Player.hp += Player.heal
            if Player.hp <= 0:
                Player.hp = 0
            print("Вы восстановили здоровье  (+{})".format(Player.heal))
            if Player.hp > Player.max_hp:
                Player.hp = Player.max_hp
            print("Текущее здоровье: {}".format(Player.hp))
            if Player.hp < 0:
                print("Вы проиграли...")
                random_event(Player)
            
        if n == "3":
            x = r.randint(1, 3)
            if x == "2":
                print("Вам удается убежать!")
                random_event(Player)
            else:
                print("Вам не удается сбежать")
        
        if enemy_hp <= 0:
            print("Вы победили, получите + 100 опыта")
            Player.exp += 100
            if Player.exp >= Player.max_exp:
                Player.exp = 0
                Player.max_exp *= 5
                Player.lvl += 1
                upgrade(Player)       
            print("Текущий опыт: {} ".format(Player.exp))


       
random_event(Player)