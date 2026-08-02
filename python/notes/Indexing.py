#indexing = [start:end:step]

number = "1234-5678-3456-7890"

print(number[:])
print(number[:9])
print(number[-10:-8])
print(number[3::2])

last_digits = number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")