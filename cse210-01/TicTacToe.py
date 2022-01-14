

boardToe = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in boardToe:
    board_keys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(boardToe)
        print("It's your turn," + turn + "choose a square (1-9):")

        move = input()        

        if boardToe[move] == ' ':
            boardToe[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if boardToe['7'] == boardToe['8'] == boardToe['9'] != ' ': 
                printBoard(boardToe)
                print("\nGood game. Thanks for playing!.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif boardToe['4'] == boardToe['5'] == boardToe['6'] != ' ': 
                printBoard(boardToe)
                print("\nGood game. Thanks for playing!.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif boardToe['1'] == boardToe['2'] == boardToe['3'] != ' ': 
                printBoard(boardToe)
                print("\nGood game. Thanks for playing!.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif boardToe['1'] == boardToe['4'] == boardToe['7'] != ' ': 
                print("\nGood game. Thanks for playing!.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif boardToe['2'] == boardToe['5'] == boardToe['8'] != ' ': 
                printBoard(boardToe)
                print("\nGood game. Thanks for playing!.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif boardToe['3'] == boardToe['6'] == boardToe['9'] != ' ': 
                printBoard(boardToe)
                print("\nGood game. Thanks for playing!.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif boardToe['7'] == boardToe['5'] == boardToe['3'] != ' ':
                printBoard(boardToe)
                print("\nGood game. Thanks for playing!.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif boardToe['1'] == boardToe['5'] == boardToe['9'] != ' ': 
                printBoard(boardToe)
                print("\nGood game. Thanks for playing!.\n")                
                print(" **** " +turn + " won. ****")
                break 

        if count == 9:
            print("\nGood game. Thanks for playing!.\n")                
            print("It's a Tie!!")

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
if __name__ == "__main__":
    game()