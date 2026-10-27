s = "Hello world"
result = []

for i in range(0, len(s)):
    if s[i] == " ":
        for k in range(s.index(" "), len(s)):
            result.insert(k - s.index(" "), s[k])
        break
    else:
        result.append(s[i])


print(result)