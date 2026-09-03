# First Exercise - Find the type
x = 4.0
x = "Cybersikkerhed"
x = 500
print(x)
print(type(x))

# Second exercise - A string program
first_name = "Liban"
last_name = "Rage"

# 1. concatenate
full_name = first_name + " " + last_name
# 2. print string
print(full_name)
# 3. print length
print(len(full_name))
# 4. print string 50 times
print(full_name * 50)
# 5. print only last character
print(full_name[-1])
# 6. check for "z"
print("z" in full_name)



#Third exercise - Split it up
full_name = "Liban Rage"

name_parts = full_name.split()  # 1. list from string
print(name_parts)  # 2. print list
print(type(name_parts))  # 3. prove it's a list

name_parts_a = full_name.split("a")  # 4. split on "a"
print(name_parts_a)

full_name_restored = " ".join(name_parts)  # 5. join back together
print(full_name_restored)

#Fourth exercise - What is the output
file_location = 'C:\\test\\new.doc'
print('File is at: ', file_location)


# Fifth exercise - Future age 
age = input("Enter your age: ")
age = int(age)

future_age = age + 100
print("In 100 years you will be", future_age)

current_year = 2026
future_year = current_year + (100 - age)
print("You will turn 100 in the year", future_year)


# Sixth exercise - Clean security log
log = "   LOGIN FAILED - USER: ALICE - IP: 192.168.10.42   "
new_log = log.lower().strip().replace("-", "|")



# Seventh exercise - Escape sequences
# 1. Two-line alert
print("SECURITY ALERT\nFailed login detected")

# 2. Columns
print("TIME\tUSER\tRESULT")
print("22:14\tadmin\tFAILED")

# 3. Message with quotation marks
print("IDS message: \"Suspicious login attempt detected\"")

# 4. File path
print("C:\\Security\\Logs\\Failed_logins.txt")