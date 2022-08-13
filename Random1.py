from dataclasses import dataclass
import sqlite3
import random

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
            

    def upgrade(self):
        if self.player_sp > 0:
            print(f"Доступны очки навыков. Кол-во очков {self.player_sp}")
            print("Нажмите 1, чтобы повысить HP на 5")
            print("Нажмите 2, чтобы повысить атаку на 1")
            print("Нажмите 3, чтобы повысить исцеление на 2")
            action = input("> ")
            if action == "1":
                self.player_hp += 5
                self.player_sp -= 1
                self.player_Mhp += 5
            elif action == "2":
                self.player_atk += 2
                self.player_sp -= 1
            elif action == "3":
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




class Enemy:
    def __init__(self, enemy_name, enemy_hp, enemy_atk, enemy_exp):
        self.enemy_name = enemy_name
        self.enemy_hp = enemy_hp
        self.enemy_atk = enemy_atk
        self.enemy_exp = enemy_exp

@dataclass    
class EnemyTemplate:
    enemy_name: str
    enemy_hp: int
    enemy_atk: int
    enemy_exp: int


# Сделать класс битва.

class Battle():

    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def attack(self):
        self.enemy.enemy_hp -= self.hero.player_atk
        print(f"Вы нанесли урон: {self.hero.player_atk}")
        self.hero.player_hp -= self.enemy.enemy_atk
        print(f"Вам нанесли урон: {self.enemy.enemy_atk}")
        if self.hero.player_hp < 0:
            print("Вы проиграли...")
            self.hero.stats_basic()
            

    def heal(self):
        self.hero.player_hp -= self.enemy.enemy_atk
        print(f"Вам нанесли урон: {self.enemy.enemy_atk}")
        self.hero.player_hp += self.hero.player_heal
        if self.hero.player_hp <= 0:
            print("Вы проиграли")
            self.hero.stats_basic()
            
        if self.hero.player_hp >= 0: 
            print(f"Вы восстановили здоровье  (+{self.hero.player_heal})")
        if self.hero.player_hp > self.hero.player_Mhp:
            self.hero.player_hp = self.hero.player_Mhp
        print(f"Текущее здоровье: {self.hero.player_hp}")

    def retreat(self):
        retreat = random.randint(1, 3)
        if retreat == 2:
            print("Вам удается убежать!")
            random_event()
            
        else:
            print("Вам не удается сбежать")
            print("Вы проиграли...")
            hero.stats_basic()
            

    def lvl_up(self):
        if self.hero.player_exp >= self.hero.player_Mexp:
            self.hero.player_exp = 0
            self.hero.player_Mexp *= 5
            self.hero.player_lvl += 1
            self.hero.player_sp += 1
            self.hero.upgrade()     
            print(f"Текущий опыт: {self.hero.player_exp} ")

    def reward(self):
        if self.enemy.enemy_hp <= 0:
            print(f"Вы победили, получите +{self.enemy.enemy_exp} ед. опыта ")
            self.enemy.enemy_hp = 0
            self.hero.player_exp += self.enemy.enemy_exp
            if self.hero.player_exp >= self.hero.player_Mexp:
                self.lvl_up()

    def start_battle(self):

        print("Вы встречаете существо " + str(self.enemy.enemy_name))
        print("Его здоровье = " + str(self.enemy.enemy_hp))
        print("Его атака = " + str(self.enemy.enemy_atk))

        while self.enemy.enemy_hp > 0:
            print("Нажмите 1, чтобы атаковать")
            print(f"Нажмите 2, чтобы вылечиться (+{self.hero.player_heal})")
            print("Нажмите 3, чтобы убежать")
            player_choice = input("> ")

            if player_choice == "1":
                self.attack()
        
            elif player_choice == "2":
                self.heal()
                
            elif player_choice == "3":
                self.retreat()
                
        self.lvl_up()
        self.reward()



def random_event(hero, enemy_list):

    while True:
        print("Что делаем?")
        print("Нажми 1, чтобы пойти сражаться")
        print("Нажми 2, чтобы проверить свои характеристики")
        answer = input("> ")
        if answer == "1":
            random_battle(hero, enemy_list)
        elif answer == "2":
            hero.check_stats()
        else:
            break
        

def random_battle(hero, enemy_list):
    
    enemy_template = random.choice(enemy_list)
    enemy = Enemy(enemy_template.enemy_name, enemy_template.enemy_hp, enemy_template.enemy_atk, enemy_template.enemy_exp)
    battle = Battle(hero, enemy)
    battle.start_battle()
    
    



if __name__ == "__main__":
    conn = sqlite3.connect('game.db') # Создание базы данных

    cur = conn.cursor() # Создаем объект cur. Он позволяет делать SQL-запросы к базе. Используем переменную cur для хранения объекта

    cur.execute("""CREATE TABLE IF NOT EXISTS Enemies(
    Enemy_name TEXT PRIMARY KEY, 
    Enemy_hp INT,
    Enemy_atk INT);  
    """) # Создаем таблицу в бд. 
    conn.commit()

    all_enemies = [('ork', '2', '1'), ('dragon', '4', '2'), ('boss', '6', '3')] # Сделать так, чтобы бд читала уже существующие объекты класса.
    cur.executemany("INSERT OR REPLACE INTO Enemies VALUES(?, ?, ?);", all_enemies)
    conn.commit()

    

    ork = EnemyTemplate("Орк", 2, 1, 2)
    dragon = EnemyTemplate("Дракон", 4, 2, 3)
    boss = EnemyTemplate("Босс", 6, 2, 5)

    enemy_list = [ork, dragon, boss]

    hero = Player(10, 10, 2, 0, 0, 0, 10, 3)
    print("Вы входите в магический куб рандома. Приготовтесь к испытаниям.")
    random_event(hero, enemy_list)
    
    

