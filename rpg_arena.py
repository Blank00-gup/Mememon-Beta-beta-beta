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
        damage_taken = damage - self.defence
        self.health -= damage_taken
        return damage_taken


    def attack(self, target):
        damage = self.strength * 2
        damage_dealt = target.take_damage(damage)
        return damage_dealt


    def is_alive(self):
        return self.health > 0

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


#print(player1.name + " vs. " + player2.name)
#print(str(player1.health) + "vs"  + str(player2.health))

#while player1.is_alive() and player2.is_alive():
    #print(player1.name + ":  " + str(player1.health))
    #print(player2.name + ":  " + str(player2.health))

    #damage = player1.attack(player2)
    #print(player1.name + " hits " + player2.name + " for " + str(damage))



def Attack2():
    damage = player1.attack(player2)
    return damage

def Eattack():
    damage = player2.attack(player1)
    return damage

def Ememe_attack():
    damage = player2.meme_attack(player1)
    return damage
def Emagic_attac():
    damage = player2.magic_attack(player1)
    return damage

def Meme_attack2():
    damage = player1.meme_attack(player2)
    return damage


def Magic_atttack2():
    damage = player1.magic_attack(player2)
    return damage




#if player1.is_alive():
    #print(player1.name + "wins")
#elif player2.is_alive():
    #print(player2.name + "wins")
#else:
    #print("tie")

