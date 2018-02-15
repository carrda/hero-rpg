#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.name = 'Generic'

    def alive(self):
        if self.name == "Zombie":
            return True
        elif self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        
        damage_coefficient = 1

        if enemy.name == "Shadow":
            my_random = random.randint(1, 10)
            # 10% of tiime will take damage
            if my_random <= 1:
                enemy.health -= self.power
            else:
                print("{} not damaged!".format(enemy.name))
                damage_coefficient = 0
                
        else:
            enemy.health -= self.power

       
        

        if self.name == "Hero":
            my_random = random.randint(1, 10)
            # 20% of time, double the damage
            if damage_coefficient == 0:
                pass
            elif my_random <= 2:
                enemy.health -= self.power
                print("{} did double damage!".format(self.name))
                damage_coefficient = 2
        
        if enemy.name == "Ogre":
            my_random = random.randint(1, 10)
            if my_random <= 3: 
                self.health -= damage_coefficient * self.power

                print("{} damaged additional {} points.".format(self.name, damage_coefficient * self.power))
        
        print("{} does {} damage to the {}.".format(self.name, damage_coefficient * self.power, enemy.name))
        if enemy.name == "Medic":
            my_random = random.randint(1, 10)
            # 20% of time, recuperate 2 health points
            if my_random <= 2:
                enemy.health += 2
                print("{} recuperated 2 health points.".format(enemy.name))
        if enemy.health <= 0 and enemy.name != "Zombie":
            print("{} is dead.".format(enemy.name))
        elif enemy.health <= 0 and enemy.name == "Zombie":
            print("{} never dies!".format(enemy.name))
        elif self.health <= 0:
            print("{} is dead.".format(self.name))

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))
                  
class Hero(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = "Hero"

class Goblin(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = "Goblin"

class Medic(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = "Medic"

class Shadow(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = "Shadow"

class Zombie(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = "Zombie"

class Ogre(Character): # 30% of time damage hero a like amount
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = "Ogre"

hero1 = Hero(100,5)
goblin1 = Goblin(100,2)
medic1 = Medic(100,2)
shadow1 = Shadow(100,5)
zombie1 = Zombie(20,2)
ogre1 = Ogre(50,2)

def main(hero, enemy):
    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight {}".format(enemy.name))
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(enemy)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.health > 0 or enemy.name == "Zombie":
            enemy.attack(hero)
 

main(hero1, ogre1)
