class Solution:
    def reverseDegree(self, s):
        alpha = ["0abcdefghijklmnopqrstuvwxyz"]
        num = [x for x in range(1,27)]
        num.reverse()

        for i in s:
            index = alpha.index(i)
            for letter in alpha:
                if letter == i:
                    index2 = alpha.index(letter)
                    print(index2)

Solution.reverseDegree("c")

