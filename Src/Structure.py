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
        # TODO return the attack value based on other's armor
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
    def __init__(self, level, name="Player", items=[], weapon=None, armor=None):
        super(PlayableCharacter, self).__init__(name, level)
        self.items = items
        self.weapon = weapon
        self.armor = armor
        # TODO add math to calculate the hp based on level

    def attack(self, other):
        # TODO check other type and call attacked function with self.weapon
        pass

    def get_xp(self, xp):
        # TODO check if over cap if do call level up
        pass

    def level_up(self):
        # TODO add level and add hp based on the level
        pass

    def use_item(self, other):
        # TODO check if other exists in self.items. is yes call used function of item and remove from self.items
        pass

    def attacked(self, other):
        # TODO remove hp based on other attack values
        pass

    def dead(self):
        # TODO end current run
        pass

    def interacted(self, other):
        if isinstance(other, BaseCharacter):
            print "{} tried to touch you. it was not plesent at all".format(other.name)
        elif isinstance(other, BaseItem):
            print "for some reason {} tried to touch you. you feel violated".format(other.name)
        else:
            print "error <{}> not a supported type in <{}>".format(type(other), self.interacted)


class Enemy(BaseCharacter):
    def __init__(self, level, name="Enemy", items=[], weapon=None, armor=None):
        super(Enemy, self).__init__(name, level)
        self.items = items
        self.weapon = weapon
        self.armor = armor
        # TODO add math to calculate the hp based on level

    def attack(self, other):
        # TODO check other type and call attacked function with self.weapon
        pass

    def use_item(self, other):
        # TODO check if other exists in self.items. is yes call used function of item and remove from self.items
        pass

    def attacked(self, other):
        # TODO remove hp based on other attack values
        pass

    def dead(self, other):
        # TODO if other is instance of playableCharacter give other gold and xp based on level
        pass

    def interacted(self, other):
        if isinstance(other, BaseCharacter):
            print "You tried to touch {}. he was not pleased".format(self.name)
        else:
            print "error <{}> not a supported type in <{}>".format(type(other), self.interacted)
