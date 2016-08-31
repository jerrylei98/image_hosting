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
    c.execute("CREATE TABLE IF NOT EXISTS login(user TEXT, password TEXT, confirmed INTEGER, email TEXT)") ##email, confirmation doable
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
=== Adds user to database.db with password hashed ===
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
    c.execute("INSERT INTO login VALUES(?,?,0,?)", (user, saltnhash(user,password),email,))
    conn.commit()
    conn.close()
    return True
