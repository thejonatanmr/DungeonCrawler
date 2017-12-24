from Structure import *

stick = BaseWeapon("stick", "a plain old stick", "Common", True)
stick.initialise(1, 3)
u_stick = BaseWeapon("Used stick", "a very old stick", "Common", True)
u_stick.initialise(1, 3)

player = PlayableCharacter(1, "John", stick)
goblin = Enemy(name="bob")
goblin.initialise(player.level, u_stick)

player.status()
goblin.status()
