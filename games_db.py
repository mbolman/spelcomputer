
import mysql.connector
import dn_secret

def take_input(max):
  choice = -1
  while choice < 1 or choice > max:
    choice = int(input())
    if choice < 1 or choice > max:
      print(f"Enter a valid choice please (between 1 and {max})")
  return choice


# def show_table():
  # pass
  
    
# Connect to database 'games'
games_db = mysql.connector.connect(
  host = "localhost",
  user = dn_secret.secret_user,
  password = dn_secret.secret_password,
  database = "spelcomputer"
)
games_cursor = games_db.cursor()

print(f"Connected to the Database spelcomputer")
print("The following tables were found: ")
games_cursor.execute("SHOW TABLES")
for x in games_cursor:
  print(x[0])
  
# Menu
print('\n')
print("Menu")
print("1. Show table")
print("2. Add a game")
print("3. Remove a game")
user_choice = take_input(3)
print(f"You've choosen: {user_choice}\n")

if user_choice == 1:
  show_table()
elif user_choice == 2:
  add_game()
else:
  remove_game()
