# anagram words = words made by using same alphabet letters
from unittest import result

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
temp = []
l1 = 0
l2 = 0
l3 = 0

result = []

for word in words:
    l1 = ord(word[0])
    l2 = ord(word[1])
    l3 = ord(word[2])

    for i in range(6):
        if ((chr(l1) in words[i]) and
            (chr(l2) in words[i]) and
            (chr(l3) in words[i])):
            temp.append(word)
            break

print(temp)