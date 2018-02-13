#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power


def main():
    hero1 = Hero(10,5)
    goblin1 = Goblin(6,2)

    while goblin1.health > 0 and hero1.health > 0:
        print("You have {} health and {} power.".format(hero1.health, hero1.power))
        print("The goblin has {} health and {} power.".format(goblin1.health, goblin1.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            goblin1.health -= hero1.power
            print("You do {} damage to the goblin.".format(hero1.power))
            if goblin1.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin1.health > 0:
            # Goblin attacks hero
            hero1.health -= goblin1.power
            print("The goblin does {} damage to you.".format(goblin1.power))
            if hero1.health <= 0:
                print("You are dead.")

main()
