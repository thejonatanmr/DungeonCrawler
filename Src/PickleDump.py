import pickle
from Structure import *
import os

working_dir = os.getcwd()
dir_list = working_dir.split("\\")
dir_list.pop()
working_dir = "\\".join(dir_list)

test_weapon = BaseWeapon("Stick", "A plain old stick", is_owned=True)
test_weapon1 = BaseWeapon("Sharpened Stick", "Careful, it's pointy", is_owned=True, rarity="Uncommon")
with open("{}\Assets\Weapons.pk".format(working_dir), "w+") as pickle_file:
    pickle.dump(test_weapon1, pickle_file, protocol=2)
    pickle.dump(test_weapon, pickle_file, protocol=2)

with open("{}\Assets\Weapons.pk".format(working_dir), "rb") as pickle_file:
    item_list = pickle.load(pickle_file)
    print item_list
