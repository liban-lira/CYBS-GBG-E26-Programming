# Exercise 1 - Boolean Logic Practice
# 1 & 2: variables representing a logged-in user with a locked account
is_logged_in = True
has_admin_rights = False
account_locked = True

# 3: compute whether access should be granted
access_granted = is_logged_in and has_admin_rights and not account_locked
print(access_granted)  # -> False

# Bonus: if/else
if access_granted:
    print("Access Granted")
else:
    print("Access Denied")
# -> Access Denied

# Extra bonus: Security Alert
if is_logged_in and account_locked:
    print("Security Alert")
# -> Security Alert


# Exercise 2 - My first list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[:4])

second_list = my_list[-3:]
print(second_list)


# Exercise 3 - Slicing
fruits = ["apple", "banana", "kiwi", "pear", "orange"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
weekdays = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]

# Fruits list
print(fruits[:3])
print(fruits[-2:])
print(fruits[1:3])

# Numbers list
print(numbers[::2])

# Weekdays list
print(weekdays[-2:])
print(weekdays[::-1])


# Exercise 4 - Security log

ips = [
    "189.19.202.26",
    "124.124.86.154",
    "111.123.147.92",
    "191.194.49.89",
    "191.194.49.89",
    "3.100.186.196",
    "17.102.131.131",
    "170.40.162.9",
    "66.23.103.242",
    "203.207.124.71",
    "3.100.186.196",
    "170.194.124.70",
    "3.100.186.196",
    "161.240.120.16",
    "37.161.17.14",
    "3.100.186.196",
    "144.182.46.41",
    "3.100.186.196",
    "67.180.5.237",
    "182.44.178.202",
]

ips.append("8.8.8.8")  # 1. add the newly reported IP
print(len(ips))  # 2. number of entries
print(ips[-5:])  # 3. latest 5 IPs (list is chronological)
print(ips.count("3.100.186.196"))  # 4. how many times this IP appears


# Exercise 5 - My 2nd list
my_list = []

my_list.append(2)
my_list.append(1)
my_list.append(3)

my_list.append("cyber")
print(my_list.index("cyber"))
my_list.remove("cyber")
my_list.sort()
print(my_list)


# Exercise 6 - Tuple Trouble
x = (1, 2, 3, 4, 5, "Liban")

x = x + ("Laura",)  # tuples are immutable — concatenation makes a NEW tuple
print(x)
# -> (1, 2, 3, 4, 5, "Liban", "Laura")
