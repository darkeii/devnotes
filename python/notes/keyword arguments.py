# keyword arguments = an argument proceses by an identifier
#                     help with readablity
#                     order of arguments doesnt matter
#             1. positional 2.defaul  3. KEYWORD   4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello(greeting="Good morning", title="Mr. ", first= "gengoku", last="kyojuro")


"""example"""
print("Hello How are you !", end=" ")           #here print is a pre-defined function of python and "end" is a keyword argument
print("1","2","3","4", sep="-")                 #here "sep" (separate) is a keyword for this print function


def get_phone(area, first, last, country= 91):
    return print(f"{country}-{area}-{first}-{last}")

get_phone("90","0504","5049")

