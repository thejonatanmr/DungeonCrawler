from Structure import *

stick = BaseWeapon("stick", "a plain old stick", 1, "Uncommon", 3, True)
player = PlayableCharacter(1, "John", stick)
goblin = Enemy(1, stick)

player.status()
goblin.status()