
power = int(input("power: "))
rng = int(input("Till number: "))


square = [pow(num, power) for num in range(0,rng+ 1) if num % 2 == 0]

for i in range(len(square)):
    print(f" {int(pow(square[i], 1/power))} : {square[i]}", end= "\n")