# ------------------HIGHEST NUMBER-------------------
a = 1
b = 2
c = 3

if a > b and a > c:
    print("a is the biggest")
elif b > a and b > c:
    print("b is the biggest")
else:
    print("c is the biggest")


# -------------------SECURITY CLEARANCE--------------------
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


# BONUS
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


# -------------------PORT NUMBER CHECKER--------------------
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


# BONUS
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


# --------------------LOGIN ATTEMPTS---------------------
login_attempts = [
    {"user": "admin", "ip": "10.0.0.5", "failed": 1},
    {"user": "admin", "ip": "203.0.113.10", "failed": 7},
    {"user": "guest", "ip": "10.0.0.8", "failed": 2},
    {"user": "root", "ip": "203.0.113.50", "failed": 5},
]
for attempt in login_attempts:
    print(f"User: {attempt['user']}")
    print(f"IP: {attempt['ip']}")
    print(f"Failed attempts: {attempt['failed']}")
    print()


# --------------------SECURITY LOG ANALYSIS---------------------

events = [
    "malware detected",
    "user login",
    "failed login",
    "file access",
    "email sent",
    "unauthorized access",
]

sus_events = [
    "failed login",
    "unauthorized access",
    "malware detected",
]

total_events = 0
suspicious_events = 0

for event in events:
    total_events += 1
    if event in sus_events:
        suspicious_events += 1
        print(f"ALERT: {event}")
    else:
        print(f"OK: {event}")

print("---")
print(f"Total events: {total_events}")
print(f"Suspicious events: {suspicious_events}")
if suspicious_events == 0:
    print("SECURE")
else:
    print("AT RISK")

# --------------------PASSWORD CHECKER--------------------
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
