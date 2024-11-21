import sqlite3

connection = sqlite3.connect('registrations.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS registrations (
  team_name TEXT,
  member_1_name TEXT,
  member_2_name TEXT,
  member_3_name TEXT
)''')

def save_registration(team_name, member_1_name, member_2_name, member_3_name):
  cursor.execute('SELECT * FROM registrations WHERE team_name = ?', (team_name,))
  existing_team = cursor.fetchone()
  if existing_team:
    return False

  cursor.execute('''INSERT INTO registrations (
    team_name,
    member_1_name,
    member_2_name,
    member_3_name
  ) VALUES (?, ?, ?, ?)''', (team_name, member_1_name, member_2_name, member_3_name))
  connection.commit()
  return True

