#------------------HIGHEST NUMBER-------------------
a = 1
b = 2
c = 3

if a > b and a > c:
    print("a is the biggest")
elif b > a and b > c:
    print("b is the biggest")
else:
    print("c is the biggest")



#-------------------SECURITY CLEARANCE--------------------
user_role = input("Enter your role: ")
security_clearance = int(input("Enter your security clearance level (1-5): "))

if user_role == "admin":
    print("Full Access")
elif user_role == "analyst" and security_clearance >= 3:
    print("Analyst Access")
elif user_role == "intern" and security_clearance >= 2:
    print("Limited Access")
elif user_role == "guest":
    print("Public Access Only")
else:
    print("Deny Access")


#BONUS
# from datetime import datetime

# user_role = input("Enter your role: ")
# security_clearance = int(input("Enter your security clearance level (1-5): "))

# current_hour = datetime.now().hour

# if current_hour < 9 or current_hour >= 17:
#     print("Access Denied: Outside of working hours (9-17)")
# elif user_role == "admin":
#     print("Full Access")
# elif user_role == "analyst" and security_clearance >= 3:
#     print("Analyst Access")
# elif user_role == "intern" and security_clearance >= 2:
#     print("Limited Access")
# elif user_role == "guest":
#     print("Public Access Only")
# else:
#     print("Deny Access")


#-------------------PORT NUMBER CHECKER--------------------
port = int(input("Enter port number: "))

match port:
    case 22:
        print("SSH - Secure Shell (Critical Security Service)")
    case 80:
        print("HTTP - Web Traffic (Unencrypted)")
    case 443:
        print("HTTPS - Secure Web Traffic")
    case 20 | 21:
        print("FTP - File Transfer (Legacy Protocol)")
    case 53:
        print("DNS - Domain Name Resolution")
    case 25:
        print("SMTP - Email Transfer")
    case other:
        print("Unknown or Custom Port - Investigate")


#BONUS
# print("\nPort Range Analysis:")
# match port:
#     case p if 1 <= p <= 1023:
#         print("Well-known system ports")
#     case p if 1024 <= p <= 49151:
#         print("Registered user ports")
#     case p if 49152 <= p <= 65535:
#         print("Dynamic/private ports")
#     case _:
#         print("Invalid port number")



#--------------------PASSWORD CHECKER--------------------
attempts = 1
while True:
    password = input("What is your password")

    if len(password) < 12:
        print("password is too short")
        attempts += 1
    elif not any(x.isdigit() for x in password):
        print("Missing number")
        attempts += 1
    else:
        print("Strong password accepted")
        break

print(attempts)


#FOR LOOP SECTION WILL BE PROVIDED DURING 
#NEXT LECTURE
