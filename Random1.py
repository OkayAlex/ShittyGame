import sqlite3
import random



conn = sqlite3.connect('game.db') # Создание базы данных

cur = conn.cursor() # Создаем объект cur. Он позволяет делать SQL-запросы к базе. Используем переменную cur для хранения объекта

cur.execute("""CREATE TABLE IF NOT EXISTS Enemies(
   Enemy_name TEXT PRIMARY KEY, 
   Enemy_hp INT,
   Enemy_atk INT);  
""") # Создаем таблицу в бд. 
conn.commit()


all_enemies = [('ork', '2', '1'), ('dragon', '4', '2'), ('boss', '6', '3')]
cur.executemany("INSERT OR REPLACE INTO Enemies VALUES(?, ?, ?);", all_enemies)
conn.commit()


class Player: 
    """Инициализация игрока"""
    def __init__(self, player_hp, player_Mhp, player_atk, player_lvl, player_sp, player_exp, player_Mexp, player_heal):
        self.player_hp = player_hp
        self.player_Mhp = player_Mhp # Player Max HP
        self.player_atk = player_atk
        self.player_lvl = player_lvl
        self.player_sp = player_sp #skill point
        self.player_exp = player_exp
        self.player_Mexp = player_Mexp # Player Max Experience
        self.player_heal = player_heal
    
    
    def stats_basic(self):
        if self.player_hp < 0:
            self.hp = 10
            self.player_Mhp = 10
            self.player_atk = 2
            self.player_lvl = 0
            self.player_sp = 0
            self.player_exp = 0
            self.player_Mexp = 10
            self.player_heal = 3
            print("Вы умерли. Начните заново")

    def upgrade(self):
        while self.player_sp > 0:
            print(f"Доступны очки навыков. Кол-во очков {self.player_sp}")
            print("Нажмите 1, чтобы повысить HP на 5")
            print("Нажмите 2, чтобы повысить атаку на 1")
            print("Нажмите 3, чтобы повысить исцеление на 2")
            action = input("> ")
        if action == "1":
            self.player_hp += 5
            self.player_sp -= 1
            self.player_Mhp += 5
        if action == "2":
            self.player_atk += 2
            self.player_sp -= 1
        if action == "3":
            self.player_heal += 1
            self.player_sp -= 1

    def check_stats(self):
        print("Ваши текущие характеристики:")
        print(f"HP: {self.player_hp}/{self.player_Mhp}")
        print(f"Атака: {self.player_atk}")
        print(f"Исцеление: {self.player_heal}")
        print(f"Опыт: {self.player_exp}/{self.player_Mexp}")
        print(f"Уровень: {self.player_lvl}")
        input("Enter чтобы продолжить")

Hero = Player(10, 10, 2, 0, 0, 0, 100, 3)


class Enemy:
    def __init__(self, enemy_name, enemy_hp, enemy_atk, enemy_exp):
        self.enemy_name = enemy_name
        self.enemy_hp = enemy_hp
        self.enemy_atk = enemy_atk
        self.enemy_exp = enemy_exp

    def battle(self):

        print("Вы встречаете существо " + str(self.enemy_name))
        print("Его здоровье = " + str(self.enemy_hp))
        print("Его атака = " + str(self.enemy_atk))

        while self.enemy_hp > 0:
            print("Нажмите 1, чтобы атаковать")
            print(f"Нажмите 2, чтобы вылечиться (+{Hero.player_heal})")
            print("Нажмите 3, чтобы убежать")
            player_choice = input("> ")

            if player_choice == "1":
                self.enemy_hp -= Hero.player_atk
                print(f"Вы нанесли урон: {Hero.player_atk}")
                Hero.player_hp -= self.enemy_atk
                print(f"Вам нанесли урон: {self.enemy_atk}")
                if Hero.player_hp < 0:
                    print("Вы проиграли...")
                    Hero.stats_basic()
                    random_event()

            if player_choice == "2":
                Hero.player_hp -= self.enemy_atk
                print(f"Вам нанесли урон: {self.enemy_atk}")
                Hero.player_hp += Hero.player_heal
                if Hero.player_hp <= 0:
                    print("Вы проиграли")
                    Hero.stats_basic()
                    random_event()
                if Hero.player_hp >= 0: 
                    print(f"Вы восстановили здоровье  (+{Hero.player_heal})")
                if Hero.player_hp > Hero.player_Mhp:
                    Hero.player_hp = Hero.player_Mhp
                print(f"Текущее здоровье: {Hero.player_hp}")
            
            if player_choice == "3":
                retreat = random.randint(1, 3)
                if retreat == 2:
                    print("Вам удается убежать!")
                    random_event()
                else:
                    print("Вам не удается сбежать")
                    print("Вы проиграли...")
                    Hero.stats_basic()
                    random_event()
         
            if Hero.player_exp >= Hero.player_Mexp:
                Hero.player_exp = 0
                Hero.player_Mexp *= 5
                Hero.player_lvl += 1
                Hero.upgrade()     
                print(f"Текущий опыт: {Hero.player_exp} ")
            
            if self.enemy_hp <= 0:
                print(f"Вы победили, получите +{self.enemy_exp} ед. опыта ")
                
ork = Enemy("Орк", 2, 1, 2)
dragon = Enemy("Дракон", 4, 2, 3)
boss = Enemy("Босс", 6, 2, 5)


print("Вы входите в магический куб рандома. Приготовтесь к испытаниям.")

def random_event():
    while True:
        print("Что делаем?")
        print("Нажми 1, чтобы пойти сражаться")
        print("Нажми 2, чтобы проверить свои характеристики")
        answer = input("> ")
        if answer == "1":
            random_battle()
        if answer == "2":
            Hero.check_stats()
        

def random_battle():
    enemies = [1,2,3]
    battle = random.choice(enemies)
    if battle == 1:
        ork.battle()
    if battle == 2:
        dragon.battle()
    if battle == 3:
        boss.battle()
    

random_event()