#Finding a missing number

def rand_list(rng):
    import random

    # creating a set with shuffled numbers within a range

    nums = []
    nums2 = []

    for i in range(1, rng + 1):
        nums.append(i)

    for k in range(len(nums)):
        p = random.choice(nums)
        nums.remove(p)
        nums2.append(p)

    nums2.pop()

    return nums2

# list till what range ?

A = rand_list(10)
print(A)

expected_sum = 0

for i in range(1, 11):
    expected_sum += i

difference = expected_sum - sum(A)

print(f"Hence, the missing number is {difference}")

