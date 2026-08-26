import random








class Character:
    def __init__(self, name, strength, health, defense, magic, meme_power):
        self.name = name
        self.strength = strength
        self.health = health
        self.defence = defense
        self.magic = magic
        self.meme_power = meme_power

    def take_damage(self, damage):
        damage_taken = max(0, damage - self.defence)
        # Prevent health from going below 0
        self.health = max(0, self.health - damage_taken)
        return damage_taken


    def attack(self, target):
        damage = self.strength * 2
        damage_dealt = target.take_damage(damage)
        return damage_dealt


    def is_alive(self):
        return self.health > 0


    def magic_attack(self, target):
        damage = self.magic
        damage_dealt = target.take_damage(damage)
        return damage_dealt


    def meme_attack(self, target):
        damage = self.strength + self.meme_power
        damage_dealt = target.take_damage(damage)
        return damage_dealt





class Doge(Character):
    def attack(self, target):
        dexterity = 35
        critical_hit = random.randint(1,  100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
        damage_dealt = target.take_damage(damage)
        return damage_dealt

    def magic_attack(self, target):
        damage = self.magic + self.meme_power
        damage_dealt = target.take_damage(damage)
        return damage_dealt






player1 = Doge("Doge", 10, 300, 5, 50, 20)
player2 = Character("Poggers", 5, 325, 5, 10, 25)
won = ""

def check_winner():
    global won
    if not player1.is_alive() and not player2.is_alive():
        won = "Tie"
    elif not player1.is_alive():
        won = player2.name
    elif not player2.is_alive():
        won = player1.name
    else:
        won = ""




def Attack2():
    global won
    if won != "" or not player1.is_alive() or not player2.is_alive():
        return 0
    damage = player1.attack(player2)
    check_winner()
    return damage

def Eattack():
    global won
    if won != "" or not player2.is_alive() or not player1.is_alive():
        return 0
    damage = player2.attack(player1)
    check_winner()
    return damage

def Ememe_attack():
    global won
    if won != "" or not player2.is_alive() or not player1.is_alive():
        return 0
    damage = player2.meme_attack(player1)
    check_winner()
    return damage

def Emagic_attac():
    global won
    if won != "" or not player2.is_alive() or not player1.is_alive():
        return 0
    damage = player2.magic_attack(player1)
    check_winner()
    return damage

def Meme_attack2():
    global won
    if won != "" or not player1.is_alive() or not player2.is_alive():
        return 0
    damage = player1.meme_attack(player2)
    check_winner()
    return damage


def Magic_atttack2():
    global won
    if won != "" or not player1.is_alive() or not player2.is_alive():
        return 0
    damage = player1.magic_attack(player2)
    check_winner()
    return damage
