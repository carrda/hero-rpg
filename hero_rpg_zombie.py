#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.name = 'Generic'

    def alive(self):
        if self.health > 0:
            return True
        elif self.health <= 0 and self.name == "Zombie":
            return True
        else:
            return False

    def attack(self, enemy):
        enemy.health -= self.power
        print("{} does {} damage to the {}.".format(self.name, self.power, enemy.name))
        if enemy.health <= 0 and enemy.name != "Zombie":
            print("{} is dead.".format(enemy.name))
        elif enemy.health <= 0 and enemy.name == "Zombie":
            print("Zombies never die!")
        if self.health <= 0 and self.name != "Zombie":
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

class Zombie(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = "Zombie"

def main():
    hero1 = Hero(10,5)
    goblin1 = Goblin(6,2)
    zombie1 = Zombie(6,2)

    while zombie1.alive() and hero1.alive():
        hero1.print_status()
        zombie1.print_status()
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero1.attack(zombie1)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        zombie1.attack(hero1)
 

main()
