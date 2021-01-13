import random
import matplotlib.pyplot as plt

vowels = "aeiouy"
cons = "bcdfghjklmnpqrstvwxyz"
current_year = 0
children  = 2
population = []

class Jackalope:
    def __init__(self, sex):
        self.name = "".join([random.choice(cons) if x % 2 else random.choice(vowels) for x in range(5)])
        self.age = 0
        self.pregnant = False
        self.sex = sex
        self.gestation = [4, 8]
        self.death = random.randint(6, 12)

jackalopes = [Jackalope("male"), Jackalope("female")]

def give_birth(jackalope):
    if jackalope.pregnant:
        for x in range(children):
            jackalopes.append(Jackalope(random.choice(["male", "female"])))


def check_mate(jackalope):
    index = jackalopes.index(jackalope)

    current = jackalopes[index]
    if current.gestation[0] <= current.age <= current.gestation[1] and not current.pregnant and current.sex == "female": 
        if index == 0:
            next = jackalopes[index + 1]
            if current.sex != next.sex:
                if next.gestation[0] <= next.age <= next.gestation[1]: 
                    current.pregnant = True
        elif index == len(jackalopes) - 1:
            previous = jackalopes[index - 1]
            if current.sex != previous.sex:
                if previous.gestation[0] <= previous.age <= previous.gestation[1]: 
                    current.pregnant = True
        else:
            next = jackalopes[index + 1]
            previous = jackalopes[index - 1]
            if current.sex != next.sex:
                if next.gestation[0] <= next.age <= next.gestation[1]: 
                    current.pregnant = True
            if current.sex != previous.sex:
                if previous.gestation[0] <= previous.age <= previous.gestation[1]: 
                    current.pregnant = True




def year(current_year):
    current_year += 1   
    for jack in jackalopes:
        jack.age += 1
        give_birth(jack)
        check_mate(jack)
        if jack.age > jack.death:
            jackalopes.remove(jack)
        random.shuffle(jackalopes)
    population.append(len(jackalopes))
    return current_year

    


while 2 <= len(jackalopes) < 10000:
    current_year = year(current_year)
else:
    print(f"It took {current_year} years to reach {len(jackalopes)} population")
    for jack in jackalopes[:10]:
        print(jack.name)

    # print(current_year, len(population))
    plt.plot(list(range(current_year)), population)
    plt.show()