class ConsoleManager:
    def __init__(self, player):
        self.player = player
        print "welcome to the Dungeon"

    def status(self, enemy=None):
        print self.player.status()
        if enemy:
            print enemy.status()

    def actions(self):
        print "Attack, Interact, Status, Exit"

    def c_print(self, string):
        print string

    @staticmethod
    def attacked(p1, p2):
        print "{} attaed {}".format(p1.name, p2.name)

    def handle_input(self, enemy=None):
        print "your actions are:"
        self.actions()
        input = raw_input("what do you want to do?")
        if input == "Status":
            self.status(enemy)
            return "s"
        elif input == "Attack":
            return "a"
        elif input == "Interact":
            return "i"
        elif input == "Exit":
            return "e"