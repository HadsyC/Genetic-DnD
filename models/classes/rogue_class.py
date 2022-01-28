from models.classes.basic_class import BasicClass
from player.stats import Stat
from other.dice import Dice


class RogueClass(BasicClass):
    def __init__(self):
        hit_dice = Dice(8, 1)
        proficiency = [Stat.DEX, Stat.INT]
        super().__init__("Rogue", hit_dice, proficiency, starting_proficiencies)

    def get_class_features(self):
        return super().get_class_features()
