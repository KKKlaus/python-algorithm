friends = ["Emily", "Kevin", "Zane", "Bob", "Ben"]
print(friends[1:])
print(friends[1:3])

Test = ["Emily", "Kevin", 2, "Bob", "Ben"]
print(Test[1:])
print(Test[1:3])

friends.extend(Test)

friends.append("Oscar")

print(friends.index("Oscar"))
print(friends.count("Oscar"))

friends.insert(1, "Kelly")

friends.remove("Kelly")

friends.pop()

friends.clear()

friends2 = friends.copy()

luckly_number = [3, 5, 8, 1, 7]
luckly_number.sort()
luckly_number.reverse()

'''
    2D lists
'''
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [9]
]
print(number_grid[2][0])
