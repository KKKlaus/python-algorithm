"""
    open(filename, mode)
    mode:
        r  : read
        w  : write
        a  : append
        r+ : read & write
"""
employees_file = open("employees.txt", "r+")


print(employees_file.readable())
# print(employees_file.readlines()[1])
# print(employees_file.readline())  # print the first line
# print(employees_file.readline())  # print the second line because the pointer points to next line
# print(employees_file.readlines())  # pointer keep moving: ['Ketchup - fullstack engineer']

for employee in employees_file.readlines():
    print(employee)

employees_file.write("\nNunie - designer")
employees_file.write("\n<p>This is HTML</p>")

employees_file.close()
