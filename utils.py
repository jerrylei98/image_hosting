from os import path
import md5
import sqlite3

if not path.isfile("database.db"):
    conn = sqlite3.connect("database.db") #creates database.db if doesn't exist
    c = conn.cursor()
    # 1 = true; 0 = false;
    #==|user      |password   |confirmed  |email    |===#
    #===================================================#
    #==|joey      |xxxxxxxxxxx|1          |joe@p.com|===#
    #==|mary      |xxxxxxxxxxx|0          |sam@a.com|===#
    # add email method to pull password?
    c.execute("CREATE TABLE IF NOT EXISTS login(user TEXT, password TEXT, confirmed INTEGER, email TEXT)") ##email, confirmation doable
    c.execute("CREATE TABLE IF NOT EXISTS images(filetype TEXT, user TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
    #timestamp DATETIME DEFAULT CURRENT_TIMESTAMP (put into id saving)
    conn.commit()
    conn.close()

"""
=== Hashes password with user ===
Input:
- user - string
- password - string
Returns: hashed password - string
"""
def saltnhash(user,password):
    m = md5.new()
    m.update(user + password)
    return m.hexdigest()

"""
=== Checks if user is in table: login ===
=== Adds user to database.db with password hasshed ===
Input:
- user - string
- password - string
Depends on fn: saltnhash(user,password)
Returns:
- True if user is added
- False if user is already taken
"""
def create_user(user, password, email):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    d = c.execute("SELECT * FROM login WHERE user = ?", (user,))
    for row in d:
        conn.commit()
        conn.close()
        return False
    c.execute("INSERT INTO login VALUES(?,?,?,?)", (user, saltnhash(user,password),0,email,))
    conn.commit()
    conn.close()
    return True

"""
===Used to authenticate user===
Input:
- user - string
- password - string
Depends on fn: saltnhash(user,password)
Returns:
- True if user+pass matches
- False if user+pass does not match
"""
def check_user(user, password):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c = c.execute("SELECT * FROM login WHERE user = ? and password = ?", (user, saltnhash(user,password),))
    for row in c:
        conn.close()
        return True
    conn.close()
    return False

def check_user_exists(user):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c = c.execute("SELECT * FROM login WHERE user = ?", (user,))
    for row in c:
        conn.close()
        return True
    conn.close()
    return False

def image_add(filetype, user):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c = c.execute("INSERT INTO images(filetype, user), VALUES(?,?)", (filetype,user))
    rowid = c.lastrowid
    conn.commit()
    conn.close()
    return rowid
