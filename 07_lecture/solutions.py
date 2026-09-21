def password_checker(password, minimum_length):
    if minimum_length < 6:
        print("Error: minimum_length must be at least 6 characters")
        return
    if minimum_length > 64:
        print("Error: minimum_length should not be above 64 characters")
        return

    if len(password) < minimum_length or len(password) < 6:
        print(f"Password is too short. Needs at least {minimum_length} characters.")
        return

    print("Password is good enough!")


# Test calls
password_checker("Cyber123!", 8)
password_checker("abc", 8)
password_checker("Cyber123!", 4)
password_checker("Cyber123!", 100)


def password_length_check(pw) -> bool:
    return len(pw) > 8


def password_number_checker(pw) -> bool:
    for char in pw:
        if char.isdigit():
            return True
    return False

def password_capital_letter_checker(pw) -> bool:
    for char in pw:
        if char.isupper():
            return True
    return False


def password_checker_02(password) -> bool:
    if not password_length_check(password):
        print("Sorry, your password is not long enough")
        return False
    if not password_number_checker(password):
        print("Sorry, your password needs numbers")
        return False
    if not password_capital_letter_checker(password):
        print("Sorry, your password needs at least one uppercase letter")
        return False
    return True


password = input("What's the password to check? ")
password_check = password_checker_02(password)

if password_check:
    print("Password check succeeded, you made a strong password")
elif not password_check:
    print("Your password is not strong. Try again.")


my_list = ["a", "b", "c"]
my_dict = {}

# Lists: accessing an index that doesn't exist -> IndexError
try:
    print(my_list[len(my_list)])
except IndexError as e:
    print(f"IndexError: {e}")

# Dictionaries: accessing a key that doesn't exist -> KeyError
try:
    print(my_dict["CYBS"])
except KeyError as e:
    print(f"KeyError: {e}")


def check_login_attempts(user_input):
    try:
        attempts = int(user_input)

        if attempts < 0:
            raise ValueError("Number of attempts cannot be negative")

        if attempts >= 5:
            return "Account locked"
        else:
            return "Access granted"

    except ValueError as e:
        print(f"Invalid input: {e}")
        return None


# Test calls covering all scenarios
print(check_login_attempts("3"))
print(check_login_attempts("7"))
print(check_login_attempts("-2"))
print(check_login_attempts("abc"))


# Bonus: keep asking until a valid, non-negative number is entered
while True:
    user_input = input("Enter number of failed login attempts: ")
    result = check_login_attempts(user_input)

    if result is not None:
        print(result)
        break
