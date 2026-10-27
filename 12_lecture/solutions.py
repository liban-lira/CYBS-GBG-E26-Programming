# ---------------------------------Exercise 1 - My First database--------------------------
from pathlib import Path
import sqlite3

path = Path.cwd().joinpath('test.db')
conn = sqlite3.connect(path)
c = conn.cursor()

query = """CREATE TABLE IF NOT EXISTS students(
             student_id INTEGER PRIMARY KEY NOT NULL,
             first_name TEXT NOT NULL,
             grade INTEGER
             )
             """

try:
    c.execute(query)
    c.execute("INSERT INTO students VALUES (?, ?, ?)", (1, "Liban", 2))
    c.execute("INSERT INTO students VALUES (?, ?, ?)", (2, "Hans", 10))
    c.execute("INSERT INTO students VALUES (?, ?, ?)", (3, "Alex", 4))
    conn.commit()
except Exception as e:
    print(e)
finally:
    conn.close()

# ---------------------------------Exercise 2 - My First Database - Continued--------------------------
conn = sqlite3.connect(path)
c = conn.cursor()

try:
    data = c.execute("SELECT * from students").fetchall()

    if not len(data):
        print("Table is empty")
    else:
        print(data)

    c.execute("DELETE from students WHERE student_id=1")
    conn.commit()
    data2 = c.execute("SELECT * from students").fetchall()
    print(data2)
    #BONUS - update:
    # c.execute("UPDATE students SET first_name='HEJ' WHERE student_id=2")
    # conn.commit()
except Exception as e:
    print(e)
finally:
    conn.close()

# ---------------------------------Exercise 4 - My First requests--------------------------

import requests

res = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(res.status_code)
print(res.headers['Content-Type'])

if res.status_code == 200:
    print(res.json()['email'])
    print(res.json()['name'])


# ---------------------------------Exercise 5 - Getting to know requests--------------------------

import requests
from requests.auth import HTTPBasicAuth

res = requests.get("https://testpages.eviltester.com/pages/auth/basic-auth/basic-auth-protected.html", auth=HTTPBasicAuth('authorized', 'password001'))

if "You were Authenticated" in res.text:
    print("YO IM AUTHENTICATED")