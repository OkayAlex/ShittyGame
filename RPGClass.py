from sys import exit
from random import randint


Exp = 0



#class Map(object):


#class Engine(object):




#class Movement(Engine):

#class Scene(object):

class Castle(object):

    def enter():
        print('''Вас ведут на казнь....
Тучи сгущаются и вы уже готовы покинуть этот мир...
Вдруг прилетает дракон и начинает все сжигать.. 
В суматохе вам удается вырваться, однако вы все еще в опасности...
Пытаясь сбежать из крепости, вы встречаете раненого имперского офицера, что вы сделаете?
Нажмите 1, чтобы помочь
Нажмите 2, чтобы пройти мимо''')
        
        action = input("> ")

        if action == "1":
            print("Вы спасаете бедолагу, и получаете плюс 10 Exp ")
            Exp =+ 10
            print('''Текущий опыт: 10. \nДо повышения уровня осталось: 90''')

        elif action == "2":
            print("Без малейшего чувства сожаления вы пробегаете вперед")
        
        else:
            print("Решай скорее, у нас мало времени")
            Castle.enter()

class Barracks(object):

    def enter():
        print('''Вы пытаетесь убежать и попадаете имперские казармы.
        Куда вы пойдете?
        Нажмите 1 - чтобы пойти вперед
        Нажмите 2 - чтобы пойти налево
        Нажмите 3 - чтобы пойти направо
        Нажмите 4 - чтобы пойти назад''')
        
        action = input("> ")

        if action == "1":
            print('''Вы идете вперед и встречаете крысу.
            Нажмите 1 - чтобы атаковать
            Нажмите 2 - чтобы попробовать проскользнуть.''')
            rat_scene = input("> ")
            if rat_scene == "1":
                Exp =+ 20
            print('''Текущий опыт: 30. \nДо повышения уровня осталось: 70''')
            if rat_scene == "2":
                print("Ты удачно обходишь крысу... ")

        elif action == "2":
            print("Ты идешь по коридору и спокойно выходишь из замка ")
            

        elif action == "3":
            print("Ты идешь направо и попадаешь в тупик. Придется вернуться назад")
            Barracks.enter()

        elif action == "4":
            print("Ты идешь назад, но попадаешь под огонь дракона. Придется начать сначала...")
            exit
           
        
        else:
            print("Решай скорее, у нас мало времени")
            Barracks.enter()



class World(object):
    situation = randint(0, 10)
    

    

#class Death(Scene):

 
#class Warrior(object):


#class Mage(object):


#class Archer(object):


#class Experience(object):


class Enemy(object):
    def __init__(self, HP, Dmg, Def):
        self.HP = HP
        self.Dmg = Dmg
        self.Def = Def

guardian = Enemy(5,5,5)
print(guardian)


        










