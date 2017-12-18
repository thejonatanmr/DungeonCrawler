import random


class BaseCharacter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attacked(self, other):
        raise NotImplementedError

    def interacted(self, other):
        raise NotImplementedError


class BaseItem:
    def __init__(self, name, desc, level, rarity, is_owned=False):
        self.name = name
        self.desc = desc
        self.level = level
        self.rarity = rarity
        self.is_owned = is_owned

    def calc_rarity_price(self):
        if self.rarity == "Common":
            return 10
        elif self.rarity == "Uncommon":
            return 50
        elif self.rarity == "Rare":
            return 100
        elif self.rarity == "Epic":
            return 1000
        elif self.rarity == "Legendary":
            return 10000

    def bought(self, other):
        raise NotImplementedError

    def use(self, other):
        raise NotImplementedError


class BaseWeapon(BaseItem):
    def __init__(self, name, desc, level, rarity, is_owned=False):
        super.__init__(name, desc, level, rarity, is_owned)
        self.price = random.randint(5, 5 * self.level, 5) + self.calc_rarity_price()

    def use(self, other):
        # TODO when enemy and character are implemented use the attacked function
        pass

    def bought(self, other):
        if not self.is_owned:
            # TODO when player character is implemented reduce the gold based on the self.price of the weapon
            self.price /= 2
            self.is_owned = True


class ConsumableItem(BaseItem):
    def __init__(self, name, desc, level, rarity, is_owned=False):
        super.__init__(name, desc, level, rarity, is_owned)
        self.price = random.randint(5, 5 * self.level, 5) + (self.calc_rarity_price() / 10)

    def use(self, other):
        # TODO when enemy and character are implemented add the desired effect
        pass

    def bought(self, other):
        if not self.is_owned:
            # TODO when player character is implemented reduce the gold based on the self.price of the weapon
            self.price /= 2
            self.is_owned = True


class PlayableCharacter(BaseCharacter):
    def __init__(self, level, name="Player"):
        super(PlayableCharacter, self).__init__(name, level)

    def attack(self, other):
        pass

    def get_xp(self, xp):
        pass

    def level_up(self):
        pass

    def use_item(self, other):
        pass

    def attacked(self, other):
        pass

    def interacted(self, other):
        pass