from random import randrange

class Pet():
    boredom_increment = 16 # play with 4 times to become full
    hunger_increment = 16 # feed 4 times to become full
    training_increment = 6.4 # train 10 times for full training
    boredom_threshold = 64 # max boredom <- bored when max
    hunger_threshold = 64 # same for here
    training_threshold = 64 # trained when max
    sounds = ['Mrrp']
    def __init__(self, name):
        self.name = name
        self.hunger = self.hunger_threshold
        self.boredom = self.boredom_threshold
        self.training = 0 # start off dumb
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        # as time increases, hunger and boredom increases
        self.boredom -= 2
        self.hunger -= 2

    def mood(self):
        if self.hunger >= self.hunger_threshold and self.boredom >= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        state += " I am" + self.training + "pts trained."
        # state += "Hunger {} Boredom {} Words {}".format(self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print (self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()
        print(self.hunger)

    def train(self):
        self.increase_training()
        print(self.training)

    def increase_training(self):
        self.training = max(training_threshold, self.training +self.training_increment)

    def reduce_hunger(self):
        self.hunger = max(hunger_threshold, self.hunger + self.hunger_increment)

    def reduce_boredom(self):
        self.boredom = max(boredom_threshold, self.boredom + self.boredom_increment)
