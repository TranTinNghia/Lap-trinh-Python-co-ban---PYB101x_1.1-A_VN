class Pokemon:
    attack = 12
    defense = 10
    health = 15
    p_type= "Normal"

    def __init__(self, name, level = 5):
        self.pokemon_name = name
        self.pokemon_level = level
    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack
    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense
    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health
    def update(self):
        self.attack_boost = 3
        self.defense_boost = 2
        self.health_boost = 5
        self.evolve = 10
    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.pokemon_level = self.pokemon_level + 1
        if self.pokemon_level % self.evolve == 0:
            return self.pokemon_level, "Evovled!"
        else:
            return self.pokemon_level
    def __str__(self):
        self.update()
        return "Pokemon name: {0}, Pokemon Type: {1}, Pokemon Level: {2} \nAttack: {3}, Defense: {4}, Health: {5}".format(self.pokemon_name, self.p_type, self.pokemon_level, self.attack, self.defense, self.health)
pokemon = Pokemon("Alomomola",9)
print(pokemon)
print("-----")
print("Training:", pokemon.train())
print("-----")
print(pokemon)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14 
    health = 12
    p_type = "Grass"
    def __init__(self, name, level = 5):
        super().__init__(name, level)
        self.weak = "Dark"
        self.strong = "Psychic"
    def update(self):
        self.attack_boost = 2
        self.defense_boost = 3
        self.health_boost = 6
        self.evovle = 12
    def train(self):
        self.update()
        self.defense_up()
        self.health_up()
        self.pokemon_level = self.pokemon_level + 1
        if self.pokemon_level > 10:
            self.attack_up()
            return self.pokemon_level
        else:
            return self.pokemon_level
    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]
    def action(self):
        return self.pokemon_name + " knows a lot of different moves!"
p1 = Grass_Pokemon("Petilil",9)
print(p1)
print("-----")
print("Training:", p1.train())
print(p1)
print("-----")
print("Training:", p1.train())
print("-----")  
print(p1)

class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"
    def __init__(self, name, level = 5):
        super().__init__(name, level)
        self.weak = "Dark"
        self.strong = "Psychic"

class Fire_Pokemon(Pokemon):
    p_type = "Fire"
    def __init__(self, name, level = 5):
        super().__init__(name, level)
        self.weak = "Water"
        self.strong = "Grass"

class Flying_Pokemon(Pokemon):
    p_type = "Flying"
    def __init__(self, name, level = 5):
        super().__init__(name, level)
        self.weak = "Electric"
        self.strong = "Fighting"

p2 = Ghost_Pokemon("Cofagrigus",10)
p3 = Fire_Pokemon("Reshiram",12)
p4 = Ghost_Pokemon("Zapdos",9)
print(p2)
print(p3)
print(p4)