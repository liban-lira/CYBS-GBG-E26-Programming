# ---------------------Reading from a file 1--------------------------

# file = open('fil.txt', 'r')
# first_line = file.readlines()
# print(first_line)


# ---------------------Reading from a file 2--------------------------

# from pathlib import Path
# cwd = Path.cwd()
# file = cwd.joinpath('l/fil.txt')
# print(file)
# print(cwd)
# file = cwd.joinpath('fil.txt')
# print(file)
# file_ob = open(file, 'r')
# print(file_ob.readline())
# file_ob.close()
# file = open('notes.txt', 'r')

# file.close()


# with open(file, 'r') as f:
#     print(f.read())


# ---------------------Writing to file--------------------------

# with open("notes.txt", "w") as f:
#     f.write("hejlkdflksdnflkds")

# with open("notes.txt", "a") as f:
#     f.write("\nhej")

# with open("notes.txt", "r") as f:
#     print(f.read())


# ---------------------Documentation exercise--------------------------

# def add_numbers(a, b):
#     """
#     Add two numbers.

#     Args:
#         a (int): First number.
#         b (int): Second number.

#     Returns:
#         int: Product of a and b.

#     Examples:
#         Add_number(1,2)
#     """
#     return a + b


# ---------------------Debug--------------------------

# def calculate_avg_age(students):
#     age = 0
#     for student in range(len(students)):
#         age = age + students[student]
#     return age / len(students)

# students = [20, 20, 30, 30]
# print (calculate_avg_age(students))
# print(list(range(len(students) -1)))
