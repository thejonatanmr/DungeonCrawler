from Structure import *
from Actors.Actors import *


def rarity_to_number(rarity):
    if rarity == "Common":
        return 0
    elif rarity == "Uncommon":
        return 1
    elif rarity == "Rare":
        return 2
    elif rarity == "Epic":
        return 3
    elif rarity == "Legendary":
        return 4


class Room:
    def __init__(self, level, gm, rarity="Common", enemy_count=1):
        self.player_level = level
        self.rarity = rarity
        self.enemy_count = enemy_count
        self.enemies = []
        self.items = []
        self.gm = gm

    def initialise(self):
        self.enemies = random.sample(enemies, self.enemy_count)
        for e in self.enemies:
            e.initialise(self.player_level)
            e.weapon.initialise(self.player_level)
        self.items = self.get_items_by_rarity()
        for i in self.items:
            i.initialise(self.player_level)
        self.gm.c_manager.c_print(random.choice(room_descs))

    def get_items_by_rarity(self):
        available_items = []
        n_rarity = rarity_to_number(self.rarity)
        for weapon in weapons:
            if weapon.rarity_to_number() <= n_rarity:
                available_items.append(weapon)
        sample_size = n_rarity + self.player_level
        return random.sample(weapons, sample_size)

    def get_enemy(self):
        if len(self.enemies) == 0:
            return None
        else:
            curr_enemy = self.enemies.pop(0)
            self.gm.c_manager.c_print("You see a {}".format(curr_enemy.name))
            return curr_enemy


class Dungeon:
    def __init__(self, player, gm):
        self.player = player
        self.room_number = 0
        self.current_room = None
        self.gm = gm

    def enter_room(self):
        self.gm.c_manager.c_print("You entered a new room")
        self.current_room = Room(self.player.level, self.gm)
        self.current_room.initialise()
        return self.current_room
