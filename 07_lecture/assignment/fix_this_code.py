def password_length_check(pw) -> bool:
    # Insert code here
    return False


def password_number_checker(pw) -> bool:
    # Insert code here
    return False


def password_capital_letter_checker(pw) -> bool:
    # Insert code here
    return False


def password_checker(password) -> bool:
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
password_check = password_checker(password)

if password_check:
    print("Password check succeeded, you made a strong password")
elif not password_check:
    print("Your password is not strong. Try again.")
