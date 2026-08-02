import random

from numpy.f2py.f90mod_rules import options
from pygments import highlight

# print(help(random))

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

# number = random.randint(low, high)                #random integer between the range given.
# number = random.random()                          #random float between 0 to 1
# number = random.choice(options)                   #chooses a random item from the tuple/list,etc   given
random.shuffle(cards)


print(cards)