from Structure import *

stick = BaseWeapon("stick", "a plain old stick", 1, "Uncommon", 3, True)

u_stick = BaseWeapon("Used stick", "a very old stick", 1, "Uncommon", 3, True, 0.5)

player = PlayableCharacter(1, "John", stick)
goblin = Enemy(1, u_stick)

player.status()
print player.weapon.use()
goblin.status()
print goblin.weapon.use()