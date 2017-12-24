import random


class BaseCharacter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attacked(self, value):
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

    def rarity_to_number(self):
        if self.rarity == "Common":
            return 0
        elif self.rarity == "Uncommon":
            return 1
        elif self.rarity == "Rare":
            return 2
        elif self.rarity == "Epic":
            return 3
        elif self.rarity == "Legendary":
            return 4

    def bought(self, buyer):
        raise NotImplementedError

    def use(self, user):
        raise NotImplementedError


class BaseWeapon(BaseItem):
    def __init__(self, name, desc, base_damage, damage_mul=1, rarity="Common", is_owned=False):
        BaseItem.__init__(self, name, desc, 1, rarity, is_owned)
        self.price = 0
        self.base_damage = base_damage
        self.damage_mul = damage_mul

    def initialise(self, level):
        self.level = level
        self.price = random.randint(5, 5 * self.level) + self.calc_rarity_price()

    def use(self):
        raw = self.base_damage
        return (raw + (random.randint(0, 3) * self.level)) * self.damage_mul

    def bought(self, buyer):
        if not self.is_owned:
            if isinstance(buyer, PlayableCharacter):
                if buyer.gold >= self.price:
                    buyer.reduce_gold(self.price)
                    self.price /= 2
                    self.is_owned = True
                else:
                    print "Error, Buyer don't have enough gold"
            else:
                print "Error, Buyer is not playable character"
        else:
            print "Error, self.is_owned is true"


class ConsumableItem(BaseItem):
    def __init__(self, name, desc, level, rarity, is_owned=False):
        BaseItem.__init__(self, name, desc, level, rarity, is_owned)
        self.price = random.randint(5, 5 * self.level, 5) + (self.calc_rarity_price() / 10)

    def use(self, user):
        # To implement - adding the desired effect
        raise NotImplementedError

    def bought(self, buyer):
        if not self.is_owned:
            if isinstance(buyer, PlayableCharacter):
                if buyer.gold >= self.price:
                    buyer.reduce_gold(self.price)
                    self.price /= 2
                    self.is_owned = True
                else:
                    print "Error, Buyer don't have enough gold"
            else:
                print "Error, <{}> is not playable character".format(type(buyer))
        else:
            print "Error, self.is_owned is true"


from Managers.ConsoleManager import *


class PlayableCharacter(BaseCharacter):
    def __init__(self, level, name="Player", weapon=None, items=[], gold=0):
        BaseCharacter.__init__(self, name, level)
        self.items = items
        self.weapon = weapon
        self.gold = gold
        self.max_hp = 90 + (self.level * 10)
        self.hp = self.max_hp
        self.xp_cap = 100 * self.level
        self.xp = 0

    def attack(self, enemy):
        if isinstance(enemy, Enemy):
            enemy.attacked(self.weapon.use())
            ConsoleManager.attacked(self, enemy)
        else:
            print "Error, <{}> is not instance of Enemy class".format(type(enemy))

    def get_xp(self, xp):
        self.xp += xp
        if self.xp >= self.xp_cap:
            self.level_up()

    def level_up(self):
        self.max_hp += 10
        self.hp = self.max_hp
        self.xp -= self.xp_cap
        self.xp_cap += 100
        self.level += 1

    def use_item(self, item):
        # TODO check if item exists in self.items. is yes call used function of item and remove from self.items
        pass

    def attacked(self, value):
        self.hp -= value

    def dead(self):
        # TODO end current run
        pass

    def is_dead(self):
        if self.hp <= 0:
            return True
        return False

    def reduce_gold(self, amount):
        if self.gold >= amount:
            self.gold -= amount
        else:
            print "Error, playable character dont have enough gold"

    def interacted(self, other):
        if isinstance(other, BaseCharacter):
            return "{} tried to touch you. it was not plesent at all".format(other.name)
        elif isinstance(other, BaseItem):
            return "for some reason {} tried to touch you. you feel violated".format(other.name)
        else:
            print "error <{}> not a supported type in <{}>".format(type(other), self.interacted)

    def status(self):
        return "---------Player--------\n" \
               "Name: {}\n" \
               "Level: {} - {}/{}\n" \
               "Hp: {}/{}\n" \
               "Weapon: {} - {} * {}\n" \
               "  - '{}'\n" \
               "-----------------------".format(self.name, self.level, self.xp, self.xp_cap, self.hp, self.max_hp,
                                                self.weapon.name, self.weapon.base_damage, self.weapon.damage_mul,
                                                self.weapon.desc)


class Enemy(BaseCharacter):
    def __init__(self, weapon=None, name="Enemy", items=[]):
        BaseCharacter.__init__(self, name, 1)
        self.items = items
        self.weapon = weapon
        self.max_hp = 0
        self.hp = self.max_hp

    def initialise(self, level):
        self.level = level
        self.max_hp = (20 * self.level) + (random.randint(1, 10) * self.level)
        self.hp = self.max_hp

    def attack(self, enemy):
        if isinstance(enemy, BaseCharacter):
            enemy.attacked(self.weapon.use())
            ConsoleManager.attacked(self, enemy)
        else:
            print "Error, <{}> is not instance of BasicCharacter class".format(type(enemy))

    def use_item(self, item):
        # TODO check if item exists in self.items. is yes call used function of item and remove from self.items
        pass

    def attacked(self, value):
        self.hp -= value

    def dead(self, other):
        if isinstance(other, PlayableCharacter):
            return [self.level * random.randint(2, 10, 2), self.level * random.randint(1, 5)]

    def is_dead(self):
        if self.hp <= 0:
            return True
        return False

    def interacted(self, other):
        if isinstance(other, BaseCharacter):
            return "You tried to touch {}. he was not pleased".format(self.name)
        else:
            print "error <{}> not a supported type in <{}>".format(type(other), self.interacted)

    def status(self):
        return "---------Player--------\n" \
               "Name: {}\n" \
               "Level: {}\n" \
               "Hp: {}/{}\n" \
               "Weapon: {} - {} * {}\n" \
               "-----------------------".format(self.name, self.level, self.hp, self.max_hp, self.weapon.name,
                                                self.weapon.base_damage, self.weapon.damage_mul)
