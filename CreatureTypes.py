import random
from BaseCreature import Creature

# method overriding (polymorphism) implements attack differently for each sub-class

class Dragon(Creature):
    def attack(self):
        damage = random.randint(10, 20)
        print(f"{self.name} breathes fire, dealing {damage} damage!")
        return damage
    
class Warrior(Creature):
    def attack(self):
        damage = random.randint(5, 15)
        print(f"{self.name} swings a sword, dealing {damage} damage!")
        return damage

class Mage(Creature):
    def attack(self):
        damage = random.randint(8, 18)
        print(f"{self.name} casts a spell, dealing {damage} damage!")
        return damage