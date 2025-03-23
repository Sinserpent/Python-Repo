#TicTacToe Attempt

#This is a simple TicTacToe game that I made in Python. It is a two player game where the players take turns to place their mark on the board. The first player to get three of their marks in a row wins the game. The game is played on a 3x3 board.

print(
'''
Tic Tac Toe
Choose A number to place a mark
1 2 3  - - -
4 5 6  - - -
7 8 9  - - -'''
)

#All Win Conditions
WinConditions=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[7,5,3],[1,4,7],[2,5,8],[3,6,9]]

#Player 1 moves Check
BlueTracker=[]


#Player 2 moves Check
RedTracker=[]

#Game State
State=[['-','-','-'],['-','-','-'],['-','-','-']]

#Counter
count = 1

#Display Current Game
def DisplayGame(S):
    for i in State:
        print('')
        for j in i:
            print(j,end=' ')
    print('')

#Valid Choice Checker
def ChoiceVerifier():
    try:
        Choice = int(input("Choose A Number: "))
        if Choice < 1 or Choice > 9:
            print("Please Select a nunber 1~9")
            return ChoiceVerifier()
        else:
            if Choice in RedTracker or Choice in BlueTracker:
                print('Choose An Empty Space')
                return ChoiceVerifier()
            else:
                return Choice
    except:
        print('Invalid Entry Try Again')
        if input() == 't':
            exit()
        else:    
            return ChoiceVerifier()
    

#Selects Space on the Board
def SpaceSelector(Choice,player):
    if Choice == 1:
        State[0][0] = player
    if Choice == 2:
        State[0][1] = player
    if Choice == 3:
        State[0][2] = player
    if Choice == 4:
        State[1][0] = player
    if Choice == 5:
        State[1][1] = player
    if Choice == 6:
        State[1][2] = player
    if Choice == 7:
        State[2][0] = player
    if Choice == 8:
        State[2][1] = player
    if Choice == 9:
        State[2][2] = player


#Checks For Wins
def WinCheck():
    match = any(set(sublist).issubset(set(RedTracker)) for sublist in WinConditions)
    if match == True:
        print("X Wins")
        exit()
    match = any(set(sublist).issubset(set(BlueTracker)) for sublist in WinConditions)
    if match == True:
        print("O Wins")
        exit()
    else:
        pass

#Updates Game State Using PLayer Choice And Who The Player is
def UpdateGameState(Choice,player):
    SpaceSelector(Choice,player)
    DisplayGame(State)
    WinCheck()
    global count
    count+=1
    if count == 10:
        print('\nDraw')
        exit()
    #State=[['1','2','3'],['4','5','6'],['7','8','9']]
    
#Starts X Turn
def RedTurn():
    print("X Turn")
    Choice = ChoiceVerifier()
    RedTracker.append(Choice)
    UpdateGameState(Choice,"X")
    BlueTurn()


#Starts O Turn
def BlueTurn():
    print("O Turn")
    Choice = ChoiceVerifier()
    BlueTracker.append(Choice)
    UpdateGameState(Choice,"O")
    RedTurn()

#Game Start
RedTurn()