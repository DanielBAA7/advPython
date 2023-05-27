class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self.__name = name
        self.__hunger = hunger

    def get_name(self):
        return self.__name

    def is_hungry(self):
        return self.__hunger > 0

    def feed(self):
        self.__hunger -= 1

    def talk(self): pass


class Dog(Animal):
    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name, hunger=0, stink_count=6):
        super(Skunk, self).__init__(name, hunger)
        self.__stink_count = stink_count

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):
    def __init__(self, name, hunger=0, color="Green"):
        super(Dragon, self).__init__(name, hunger)
        self.__color = color

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    dog = Dog("Brownie", 10)
    dog2 = Dog("Doggo", 80)
    cat = Cat("Zelda", 3)
    cat2 = Cat("Kitty", 80)
    skunk = Skunk("Stinky")
    skunk2 = Skunk("Stinky Jr.", 80)
    unicorn = Unicorn("Keith", 7)
    unicorn2 = Unicorn("Clair", 80)
    dragon = Dragon("Lizzy", 1450)
    dragon2 = Dragon("McFly", 80)
    zoo_lst = [dog, cat, skunk, unicorn, dragon, dog2, cat2, skunk2, unicorn2, dragon2]
    for animal in zoo_lst:
        # print details if animal hungry
        if animal.is_hungry():
            print(str(animal.__class__.__name__) + " " + animal.get_name())

        # feed till full
        while animal.is_hungry():
            animal.feed()

        # each animal talks its unique phrase
        animal.talk()

        # do unique action for the animal type
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(Animal.zoo_name)


if __name__ == '__main__':
    main()
