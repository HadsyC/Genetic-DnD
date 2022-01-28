import random


class Dice:
    def __init__(self, faces: int, amount: int):
        self.faces = faces
        self.amount = amount

    def roll(self):
        result = 0
        for _ in range(self.amount):
            result += random.randint(1, self.faces)
        return result
