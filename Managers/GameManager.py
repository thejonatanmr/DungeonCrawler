from Src.Structure import *
from Src.Dungeon import *
from ConsoleManager import *


class GameManager:
    def __init__(self):
        self.player = PlayableCharacter(1, "John", weapons[1])
        self.current_room = None
        self.alive = True
        self.Dungeon = Dungeon(self.player, self)
        self.c_manager = ConsoleManager(self.player)
        self.curr_enemy = None
        self.game_loop()

    def game_loop(self):
        while self.alive:
            if self.current_room is None:
                self.current_room = self.Dungeon.enter_room()
                self.curr_enemy = self.current_room.get_enemy()

            input = self.c_manager.handle_input(self.curr_enemy)
            if input == "a":
                self.player.attack(self.curr_enemy)
                self.curr_enemy.attack(self.player)
            if input == "i":
                self.c_manager.c_print(self.curr_enemy.interacted(self.player))
                self.curr_enemy.attack(self.player)
            elif input == "s":
                continue
            elif input == "e":
                self.alive = False


gm = GameManager()
