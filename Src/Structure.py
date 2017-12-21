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

    def bought(self, buyer):
        raise NotImplementedError

    def use(self, user):
        raise NotImplementedError


class BaseWeapon(BaseItem):
    def __init__(self, name, desc, level, rarity, is_owned=False):
        super.__init__(name, desc, level, rarity, is_owned)
        self.price = random.randint(5, 5 * self.level, 5) + self.calc_rarity_price()

    def use(self, user):
        # To Implement - return the attack value (no need for user)
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
                print "Error, Buyer is not playable character"
        else:
            print "Error, self.is_owned is true"


class ConsumableItem(BaseItem):
    def __init__(self, name, desc, level, rarity, is_owned=False):
        super.__init__(name, desc, level, rarity, is_owned)
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
                print "Error, Buyer is not playable character"
        else:
            print "Error, self.is_owned is true"


class PlayableCharacter(BaseCharacter):
    def __init__(self, level, name="Player", items=[], gold=0, weapon=None):
        super(PlayableCharacter, self).__init__(name, level)
        self.items = items
        self.weapon = weapon
        self.gold = gold
        self.hp = 90 + (self.level * 10)
        self.xp_cap = 100 * self.level

    def attack(self, enemy):
        if isinstance(enemy, Enemy):
            enemy.attacked(self.weapon.use())
        else:
            print "Error, enemy is not instance of Enemy class"

    def get_xp(self, xp):
        self.xp += xp
        if self.xp >= self.xp_cap:
            self.level_up()

    def level_up(self):
        self.hp += 10
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

    def attack(self, enemy):
        if isinstance(enemy, BaseCharacter):
            enemy.attacked(self.weapon.use())
        else:
            print "Error, enemy is not instance of BasicCharacter class"

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
            print "You tried to touch {}. he was not pleased".format(self.name)
        else:
            print "error <{}> not a supported type in <{}>".format(type(other), self.interacted)
