from CreatureTypes import *
import random

def battle(c1, c2):
    print(f"\nBattle begins between {c1.name} and {c2.name}!\n")

    while c1.health > 0 and c2.health > 0:
        c2.take_damage(c1.attack())
        if c2.health <= 0:
            print(f"\n{c2.name} has been defeated! {c1.name} wins!\n")
            break

        c1.take_damage(c2.attack())
        if c1.health <= 0:
            print(f"\n{c1.name} has been defeated! {c2.name} wins!\n")
            break

def reset_battle():
    # reset all creatures to full health
    for creature in creatures:
        creature.reset_health()



# usage
buarrtyl = Dragon("Buarrtyl", 50)
kekious = Dragon("Kekious", 50)
modus = Warrior("Modus", 50)
philyn = Mage("Phylin", 50)

creatures = [buarrtyl, kekious, modus, philyn]

# selective matching
battle(modus, philyn)

print("Next match!") 
reset_battle()

# choose two random, unique creatures for battle 
c1 = random.choice(creatures)
c2 = random.choice(creatures)

while c1 == c2: c1 = random.choice(creatures)

battle(c1, c2)