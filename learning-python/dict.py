month_to_num = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3
}

print(month_to_num["Jan"])
# print(map["test"])  # throw error
print(month_to_num.get("Jan"))  # the same
print(month_to_num.get("test"))  # print None
print(month_to_num.get("test", "Not a valid key"))  # we can assign the default

