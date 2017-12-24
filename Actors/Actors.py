# temporary workaround.
from Src.Structure import *


weapons = [BaseWeapon("LongSword", "A long sword", 5, rarity="Uncommon", is_owned=True),
           BaseWeapon("Broken Sword", "An old rusty sword", 3, rarity="Common", is_owned=True),
           BaseWeapon("GreatSword", "So much wow, much great", 7, rarity="Rare", is_owned=True)]

enemy_sword = BaseWeapon("LongSword", "A long sword", 5, damage_mul=0.5, is_owned=True)
enemy_hammer = BaseWeapon("Hammer", "Crush!", 5, damage_mul=0.5, is_owned=True)

enemies = [Enemy(enemy_hammer, name="Orc"), Enemy(enemy_sword, name="Goblin")]

room_descs = ["This is an old room, You smell the rot all around", "This room is somewhat new",
              "This room is very well built, You can see its old but still standing"]
