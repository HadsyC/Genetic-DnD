import json

classes_folder = 'data/class/'
rogue_file = 'class-rogue.json'

with open(f'{classes_folder}{rogue_file}', 'r') as f:
    rogue = json.load(f)

class_name = rogue['class']
