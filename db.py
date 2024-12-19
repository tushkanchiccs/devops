import psycopg2

DB_HOST = 'localhost'
DB_NAME = 'registration'
DB_USER = 'user'
DB_PASSWORD = 'password'

def insert_user(team_name, captain, teammate1, teammate2):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO teams (team_name, captain, teammate1, teammate2) VALUES (%s,%s, %s, %s)",
                        (team_name, captain, teammate1, teammate2))
        conn.commit()
        cursor.close()
        conn.close()
    except psycopg2.OperationalError as e:
        print(f"Ошибка подключения к базе данных: {e}")
        raise

def get_teams():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teams")
        teams = cursor.fetchall()
        cursor.close()
        conn.close()
        return teams
    except psycopg2.OperationalError as e:
        print(f"Ошибка подключения к базе данных: {e}")
        raise

