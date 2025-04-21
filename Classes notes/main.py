#Vincent Johnson classes notes

class subject:
    def __init__(self, content, period, teacher, room):
        self.content = content
        self.period = period
        self.teacher = teacher
        self.room = room

first = subject("CSP", 1, "Me", 200)
second = subject("CS1400", 2, "Me", 200)

print(first.content)


class pokemon:
    def __init__(self, name, species, hp, dmg):
        self.name = name
        self.species = species
        self.hp = hp
        self.dmg = dmg

    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            self.hp -= opponent.dmg
            print(f"{opponent.name} attacked {self.name} for {opponent.dmg} damage!")
            print(f"{self.name} has {self.hp} hp left.")
            if self.hp <= 0:
                print(f"{self.name} fainted!")
                print(f"{opponent.name} wins!")
                break
            else:
                opponent.hp -= self.dmg
                print(f"{self.name} attacked {opponent.name} for {self.dmg} damage!")
                print(f"{opponent.name} has {opponent.hp} hp left.")
                if opponent.hp <= 0:
                    print(f"{opponent.name} fainted!")
                    print(f"{self.name} wins!")
                    break

    def __str__(self):
        return f"{self.name} is at {self.hp} hp and is a {self.species} type pokemon. It deals {self.dmg} damage."
    
fluffy = pokemon("Fluffy", "Arcanine", 280, 110)

slimy = pokemon("Slimy", "Ditto", 100, 70)

spiky = pokemon("Spiky", "Jolt-ee-on", 1, 50000)


fluffy.battle(spiky)

slimy.battle(spiky)


'''
What is a class in python?
    A class is a blueprint for creating objects.
What is an object in python?
    An object is an instance of a class.
How do python classes relate to python objects?
    Classes are blueprints for objects. Objects are instances of classes.
How do you create a class in python?
    You create a class in python using the class keyword.
What are the methods?
    Methods are functions that belong to a class.
How do you create an object in python?
    You create an object in python by calling the class.
How do you call a method for an object?
    You call a method in python by using the dot operator.
Why do we use python classes?
    We use classes to create objects that have attributes and methods.
'''