#format specifiers = {value:flags} format a value based on whatr flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# .(number) = allocate that many spaces
# 03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center allign
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position value
# :(number)  = insert a space before positive position
# :, = comma separator

price1 = 300347512.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is ${price1: .1f}")
print(f"price 2 is ${price2:10}")
print(f"price 3 is ${price3: 010}")
print(f"price 1 is ${price1: }")
print(f"price 1 is ${price1: ,}")
print(f"price 1 is ${price1:^+,.2f}")



