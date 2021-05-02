matrix = [[" ", " ", " "]
        , [" ", " ", " "]
        , [" ", " ", " "]]

def switch(t):
    if t == 'X':
        t = 'O'
    else:
        t = 'X'
    return t

def show():
    print("\nCurrent Situation : \n")
    print(" " + matrix[0][0] + " |  " + matrix[0][1] + "  | " + matrix[0][2])
    print("---+-----+---")
    print(" " + matrix[1][0] + " |  " + matrix[1][1] + "  | " + matrix[1][2])
    print("---+-----+---")
    print(" " + matrix[2][0] + " |  " + matrix[2][1] + "  | " + matrix[2][2])
    

def turn(player):
    x = input("Its " + player + "'s Turn : ")
    
    if len(x) == 2 and int(x[0]) >= 1 and int(x[1]) >=1:
        pos = matrix[int(x[0])-1][int(x[1])-1] 
        if pos != " ":
            print('\nNumber Already Declared\n')
            return False
        else:
            matrix[int(x[0])-1][int(x[1])-1] = player
            return True
    else:
        show_allowed_format()
        return False


def check_win(player):
    for i  in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == player or matrix[i].count(player) == 3:                                                 
            print("\n"+player + " Wins!!")
            return True
        if matrix[0][0] == matrix[1][1] == matrix[2][2] == player or matrix[0][2] == matrix[1][1] == matrix[2][0] == player:
            print("\n"+player + " Wins!!")
            return True
            
        
def check_tie():
    if " " not in matrix[0] and " " not in matrix[1] and " " not in matrix[2]:
        print("\nits a tie")
        return True


def show_allowed_format():
    print("The game takes input in the following format without spaces :- \n")
    print("11" + " | " + "12" + " | " + "13")
    print("---+----+---")
    print("21" + " | " + "22" + " | " + "23")
    print("---+----+---")
    print("31" + " | " + "32" + " | " + "33")
    

def show_instructions():
    print("The numbers shown below on the tic-tac-toe board represents their respective positions.")
    print("You have to input the number. For instace :- if you have to mark on top left corner you have to enter 11 as shown in the tic-tac-toe board.")

show_instructions()
show_allowed_format()
p = 'X'
while True:
    try:
        if turn(p):
            show()
            if check_win(p) or check_tie():
                break
            p = switch(p)
            
    except IndexError:
        show_allowed_format()
    except ValueError:
        show_allowed_format()
