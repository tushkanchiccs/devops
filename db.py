import sqlite3

DB_NAME = "db"

def __init__():
    conn = db_connect()
    conn.cursor().execute("""CREATE TABLE IF NOT EXISTS teams(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    team_name VARCHAR(30),
    captain TEXT,
    teammate1 TEXT,
    teammate2 TEXT
);""")


def db_connect()->sqlite3.Connection:
    try:
        conn = sqlite3.connect(
                f"./db/{DB_NAME}.db"
            )
        return conn
    except sqlite3.OperationalError as e:
        print(f"Ошибка подключения к базе данных: {e}")
        raise

def insert_user(team_name, captain, teammate1, teammate2):
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO teams (team_name, captain, teammate1, teammate2) VALUES (?,?, ?, ?)",
                        [team_name, captain, teammate1, teammate2])
        conn.commit()
        cursor.close()
        conn.close()
    

def get_teams():
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teams")
    teams = cursor.fetchall()
    cursor.close()
    conn.close()
    return teams



__init__()

