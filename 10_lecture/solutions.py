import json
import csv


# ---------------------Your first JSON FILE--------------------------

# with open("me.json", 'r') as f:
#     data = json.load(f)

# print(f"Hello {data['name']}. You are in year {data['year']}")

# data['year'] = 2

# with open("me_updated.json", 'w') as f:
#     json.dump(data, f, indent=4)


# ---------------------JSON Security Alert--------------------------

# with open("alert.json", 'r') as f:
#     data = json.load(f)

# print(f"Alert {data['alert_id']}: {data['severity'].upper()} severity {data['alert_type']} from {data['source_ip']}")


# ---------------------Warm-up: Read and Write a CSV--------------------------

# with open("ports.csv", 'r') as f:
#     reader = csv.reader(f)
#     header = next(f)

#     for row in reader:
#         Extract the rows from row:
#         port, service = row
#         print(f"Port {port} is used by {service}")

# rows = [['computer1', '10.20.30.50'], ['computer2', '192.168.1.50']]

# with open("my_hosts.csv", 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(["hostname", "ip"])
#     writer.writerows(rows)



# -----------------THREAT INTELLIGENCE-------------------------
# -----------------Lavet af Daniel-------------------------
# import json
# import csv
# from pathlib import Path

# Opens the wanted threat inteligence (needs to be edited so it fits your location!)
# with open(Path.cwd().joinpath('Opgave-1/Threat_inteligence.json'), 'r') as file:
#     json_data = json.load(file)

# List for Tthreats that are within the scope
# threats = []

# For loop that opens the threat data in "indicators"
# because indicators has all the threat alerts
# for row in json_data["indicators"]:
        # if row["severity"] == "high" and int(row["confidence"]) > 80:
            # Appends in a list because CSV needs a list with every 
            # wanted row i a list within the list to append
            # threats.append([row["ioc_value"], row["ioc_type"], row["severity"], row["confidence"], row["last_seen"]])

# Writes the threats (that triggered the if statement above)
# To the CSV file
# Path needs to be updated!
# with open(Path.cwd().joinpath('Opgave-1/high_priority_threats.csv'), 'w', newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(["IOC","Type","Severity","Confidence","Last_Seen"])
#     csv_writer.writerows(threats)

# Reads the CSV file (just to check the CSV without changing files)
# with open(Path.cwd().joinpath('Opgave-1/high_priority_threats.csv'), 'r') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)

# 4. Counts how many alerts
# print(f"There is {len(threats)} alerts")


# 2. Filter for threats with confidence > 80 and severity = 'high'
# 3. Export filtered threats to high_priority_threats.csv
# 4. Print total count of high-priority threats found



# ---------------------Warm-up: Your First Module--------------------------

# from calc import add
# # import calc
# print(add(1,2))




# ---------------------Requests--------------------------
# import requests

# req = requests.get('https://jsonplaceholder.typicode.com/posts/1')
# print(req.status_code)
# print(req.json())