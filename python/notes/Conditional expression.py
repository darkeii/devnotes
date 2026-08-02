# one liner shortcut of the if statement (ternary operator)
# pring or assign one of two values based on a condition
# x if condition else y

num = int(input("number: "))
num2 = int(input("num2: "))
print("positive" if num > 0 else "negative")
print("Even" if num%2 == 0 else "Odd")

max_num = num if num > num2 else num2
print(max_num)
