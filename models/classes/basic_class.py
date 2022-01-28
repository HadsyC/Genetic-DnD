from abc import ABC, abstractmethod, abstractstaticmethod
from other.dice import Dice


class BasicClass(ABC):
    def __init__(self, name: str, hd: Dice, proficiency: list, starting_proficiencies: list):
        self.name = name
        self.hit_dice = hd
        self.proficiency = proficiency
        self.starting_proficiencies = starting_proficiencies

    @abstractmethod
    def get_class_features(self):
        pass

    def get_stats(self):
        return self.stats
