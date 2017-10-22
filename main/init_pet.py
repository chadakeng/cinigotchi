from random import randint

class Pet():
    happiness_increment = 16 # play with 4 times to become full
    hunger_increment = 16 # feed 4 times to become full
    training_increment = 6.4 # train 10 times for full training
    skill_inc_win = 4 # skill increment from winning game/ school
    skill_inc_food = 2 # skill increment from food
    happiness_max = 64 # max happiness <- bored when max
    training_max = 64 # trained when max
    skill_max = 640
    hunger_max = 64
    sounds = ['Mrrp']
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender #randint(0,1) girl if 0, guy if 1
        self.hunger = 0
        self.happiness = self.happiness_max
        self.training = 0 # start off dumb
        self. money = 0 # start off broke
        self.weight = 0 #lightweight scrub
        self.age = 0
        self.pencil = 0
        self.star = 0
        self.flower = 0

        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        # as time increases, hunger and happiness increases
        self.happiness -= 2
        self.hunger -= 2

    def mood(self):
        if self.hunger >= self.hunger_max and self.happiness >= self.happiness_max:
            return "happy"
        elif self.hunger > self.hunger_max:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        state += " I am" + self.training + "pts trained."
        # state += "Hunger {} happiness {} Words {}".format(self.hunger, self.happiness, self.sounds)
        return state

    def hi(self):
        print (self.sounds[randrange(len(self.sounds))])
        self.reduce_happiness()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_happiness()

    def feed(self):
        self.reduce_hunger()
        print(self.hunger)

    def train(self):
        self.inc_training()
        print(self.training)

    def increase_pencil(self, incVal):
        # increment value: food +1 - +3, game win + 4
        self.pencil = self.pencil + incVal

    def inc_training(self):
        self.training = self.training +self.training_increment

    def reduce_happiness(self):
        self.happiness = self.happiness + self.happiness_increment

    def reduce_hunger(self):
        self.hunger = self.hunger + self.hunger_increment

"""pet = Pet("sean")
print(pet.hunger)
pet.clock_tick()
pet.feed()
pet.clock_tick()
print(pet.hunger)
print(pet.gender)"""
