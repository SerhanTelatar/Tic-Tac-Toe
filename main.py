def choose_side():
  side = input("Player1, please choose your side (either X or O): ")
  while True:
    if side == "X":
      return side
    elif side == "O":
      return side
    else:
      side = input("Player1, please choose your side (either X or O): ")

def display_enviroment(list):
  print(list[0][0] + "|" + list[0][1] + "|" + list[0][2])
  print("-+-+-")
  print(list[1][0] + "|" + list[1][1] + "|" + list[1][2])
  print("-+-+-")
  print(list[2][0] + "|" + list[2][1] + "|" + list[2][2])

def makechoice(num):
  if num == "1":
    location = input("Player1, please make your choice: ")
    location_list = location.split(",")

    num_location_list = []

    for each in location_list:
      each = int(each)
      num_location_list.append(each)
  else:
    location = input("Player2, please make your choice: ")
    location_list = location.split(",")

    num_location_list = []

    for each in location_list:
      each = int(each)
      num_location_list.append(each)
  return num_location_list

def implychoices(field, choice, player):
  loc1 = int(choice[0])
  loc2 = int(choice[1])
  str_loc = f"{loc1},{loc2}"
  if field[loc1][loc2] != " ":
    a = field[loc1][loc2]
    print(f"{a} is already in the location {str_loc}. Skipping this turn.")
    return field
  else:
    field[loc1][loc2] = player
    return field

def checkboard(list):
  checker = 0
  for each in range(len(list)):
    for a in list[each]:
      if a == " ":
        checker +=1
  if checker == 0:
    return False
  return True

def is_winner(list):
  if list[0][0] == list[1][1] == list[2][2]:
    winner = list[0][0]
    return winner
  if list[0][2] == list[1][1] == list[2][0]:
    winner = list[0][2]
    return winner
  for each in list:
    amount_x = each.count("X")
    amount_o = each.count("O")
    if amount_x == 3:
      winner = "X"
      return winner
    if amount_o == 3:
      winner = "O"
      return winner
  for i in range(3):
    vertically = []
    for each in list:
      vertically.append(each[i])
    amount_x = vertically.count("X")
    amount_o = vertically.count("O")
    if amount_x == 3:
      winner = "X"
      return winner
    if amount_o == 3:
      winner = "O"
      return winner


print("Welcome to the Tic-Tac-Toe Game!")
player1 = choose_side()
if player1 == "X":
  player2 = "O"
else:
  player2 = "X"

field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
display_enviroment(field)

while True:
  player1_choice = makechoice("1")
  field = implychoices(field, player1_choice, player1)
  display_enviroment(field)
  if is_winner(field) == player1 or checkboard(field) == False:
    break

  player2_choice = makechoice("2")
  field = implychoices(field, player2_choice, player2)
  display_enviroment(field)
  if is_winner(field) == player2 or checkboard(field) == False:
    break

if checkboard(field) == False:
  print("The game is finished! It is a tie.")

else:
  if player1 == is_winner(field):
    print("Player1 has won the game!")

  else:
    print("Player2 has won the game!")