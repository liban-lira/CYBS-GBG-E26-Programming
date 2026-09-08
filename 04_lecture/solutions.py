# ---------BOOK PRICES-------------------------------
book_prices = {}

book_prices["Lord of the Rings"] = 150
book_prices["Cybersikkerhed 101"] = 500
book_prices["Mad Max"] = 399
print(book_prices)

print(book_prices["Mad Max"])

print(book_prices.get("The Hobbit"))  # None, since it's not in the dictionary

book_prices["Lord of the Rings"] = 200
print(book_prices)

book_prices["Dune"] = 250
print(book_prices)

del book_prices["Cybersikkerhed 101"]
print(book_prices)

print("Cybersikkerhed 101" in book_prices)  # False
print("Mad Max" in book_prices)  # True


# ---------USER ROLES-------------------------------

user_roles = {"admin": "Laura", "moderator": "Liban", "guest": "unknown"}

print(user_roles.keys())

print(user_roles.get("moderator"))

del user_roles["guest"]
print(user_roles)

print(len(user_roles))

user_roles["admin"] = "Alex"

# or use update
# user_roles.update({"admin": 'Alex'})
print(user_roles)

user_roles["auditor"] = "Alice"

# or use update
# user_roles.update({"auditor": 'Alice'})

print(user_roles)


# ---------SECURITY LOG-------------------------------

incidents = {
    "INC-1042": {"reported_by": "Liban", "severity": "high"},
    "INC-1043": {"reported_by": "Laura", "severity": "medium"},
}

print(incidents["INC-1042"]["severity"])

incidents["INC-1042"]["status"] = "open"
print(incidents)

incidents["INC-1044"] = {"reported_by": "Alex", "severity": "low"}
print(incidents)

incidents["INC-1043"]["severity"] = "high"
print(incidents)

print(len(incidents))

print(incidents)


# ---------BLOCKED IPS-------------------------------
blocked_ips = {"10.0.0.5", "192.168.1.100", "172.16.0.50"}
new_threats = {"192.168.1.100", "10.0.0.99", "8.8.8.8"}

print(blocked_ips)

blocked_ips.add("203.0.113.0")
print(blocked_ips)

print("8.8.8.8" in blocked_ips)  # False

print(blocked_ips.intersection(new_threats))  # {'192.168.1.100'}

combined = blocked_ips.union(new_threats)
print(combined)

blocked_ips.remove("10.0.0.5")
print(blocked_ips)


# ---------MALWARE CHECKER-------------------------------
scan_a = {"7f3a9b", "c81de2", "45bb01", "9e0f77"}
scan_b = {"c81de2", "9e0f77", "220ac4", "de91f0"}

new_scan = scan_a.union(scan_b)
print(len(new_scan))  # 6 unique

print("45bb01" in scan_b)  # False
print("220ac4" in scan_a)  # False

scan_a.add("8899ff")
print(scan_a)

print(len(scan_a))  # 5

print(scan_a.union(scan_b))


# ---------LOGIN ATTEMPTS-------------------------------
login_1 = {"user": "admin", "ip": "10.0.0.5"}
login_2 = {"user": "admin", "ip": "192.168.1.100"}
login_3 = {"user": "guest", "ip": "10.0.0.5"}
login_4 = {"user": "root", "ip": "203.0.113.9"}

unique_ips = set()
unique_ips.add(login_1["ip"])
unique_ips.add(login_2["ip"])
unique_ips.add(login_3["ip"])
unique_ips.add(login_4["ip"])
print(len(unique_ips))  # 3

login_counts = {}
login_counts[login_1["user"]] = 1
login_counts[login_2["user"]] = 2
login_counts[login_3["user"]] = 1
login_counts[login_4["user"]] = 1

print(login_counts)
print(unique_ips)
