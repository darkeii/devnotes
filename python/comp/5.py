# counting vowels and consonants

s = input(">> ").lower()

v = 0
c = 0

for letter in s:
    if ord(letter) <= 122 and ord(letter) >= 97:
        match ord(letter):
            case 97:
                v += 1
            case 101:
                v += 1
            case 105:
                v += 1
            case 111:
                v += 1
            case 117:
                v += 1
            case _:
                c += 1


print(f"Vovels: {v}")
print(f"Consonants: {c}")

