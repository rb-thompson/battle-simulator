from abc import ABC, abstractmethod

# abstract base classes use ABC to enforce common behavior
class Creature(ABC):
    def __init__(self, name, health):
        self. name = name
        self.health = health
        self.health_arg = health
    
    @abstractmethod
    def attack(self):
        """Each creature will have a unique attack method"""
        pass

    # encapsulation by protecting 'health' and modifying only via take_damage()
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Remaining health: {self.health}")

    def reset_health(self):
        self.health = self.health_arg