# for  loops = execute a code a fixed number of times.
#              You can iterate over a range , string, sequence, etc

for x in reversed(range(1,11,2)):
    print(x)

print("Happy new year !")

credit_card = "1234-5678-2345-6789"

for x in credit_card:
    print(x)

for  x in range(1,23):
    if x == 13:
        continue        #skips and continues the loop
    else:
        print(x)



