from random import randrange
def display_board(board):
    one = board[0][0]
    two = board[0][1]
    three = board[0][2]
    four = board[1][0]
    five = board[1][1]
    six = board[1][2]
    seven = board[2][0]
    eight = board[2][1]
    nine = board[2][2]
    print("+-------+-------+-------+")
    print("|\t|\t|\t|")
    print(f"|   {one}\t|   {two}\t|   {three}\t|")
    print("|\t|\t|\t|")
    print("+-------+-------+-------+")
    print("|\t|\t|\t|")
    print(f"|   {four}\t|   {five}\t|   {six}\t|")
    print("|\t|\t|\t|")
    print("+-------+-------+-------+")
    print("|\t|\t|\t|")
    print(f"|   {seven}\t|   {eight}\t|   {nine}\t|")
    print("|\t|\t|\t|")
    print("+-------+-------+-------+")

#The computer puts it's move always in the center
#You can choose your move from 1 to 9 except 5 because that is the center
def enter_move(board):
    while True:
        move = int(input("Please enter your move: "))
        if move not in moves_used and move <= 9 and move > 0 and move != 5:
            if move == 1:
                moves_used.append(1)
                remain_moves.remove(1)
                board[0][0] = "O"
                break

            elif move == 2:
                moves_used.append(2)
                remain_moves.remove(2)
                board[0][1] = "O"
                break

            elif move == 3:
                moves_used.append(3)
                remain_moves.remove(3)
                board[0][2] = "O"
                break

            elif move == 4:
                moves_used.append(4)
                remain_moves.remove(4)
                board[1][0] = "O"
                break

            elif move == 6:
                moves_used.append(6)
                remain_moves.remove(6)
                board[1][2] = "O"
                break

            elif move == 7:
                moves_used.append(7)
                remain_moves.remove(7)
                board[2][0] = "O"
                break

            elif move == 8:
                moves_used.append(8)
                remain_moves.remove(8)
                board[2][1] = "O"
                break

            elif move == 9:
                moves_used.append(9)
                remain_moves.remove(9)
                board[2][2] = "O"
                break
        else:
            print("That space has been chosen already")
def make_list_of_free_fields(board):
    return "pending"
#
def VictoryFor(board, sign):
    if sign == "X":
        if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
            #print("AI Won!")
            return True
        elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
            #print("AI Won!")
            return True
        elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
            #print("AI Won!")
            return True
        elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
            #print("AI Won!")
            return True
        elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
            #print("AI Won!")
            return True
        elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            #print("AI Won!")
            return True
        elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
            #print("AI Won!")
            return True
        elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
            #print("AI Won!")
            return True
    elif sign == "O":
        if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
            #print("You Won!")
            return True
        elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
            #print("You Won!")
            return True
        elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
            #print("You Won!")
            return True
        elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
            #print("You Won!")
            return True
        elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
            #print("You Won!")
            return True
        elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            #print("You Won!")
            return True
        elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
            #print("You Won!")
            return True
        elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
            #print("You Won!")
            return True

def DrawMove(board):
    while True:
        move_ai = randrange(10)
        if move_ai not in moves_used and move_ai <= 9 and move_ai > 0 and move_ai != 5:
            if move_ai == 1:
                moves_used.append(1)
                remain_moves.remove(1)
                board[0][0] = "X"
                break

            elif move_ai == 2:
                moves_used.append(2)
                remain_moves.remove(2)
                board[0][1] = "X"
                break
            elif move_ai == 3:
                moves_used.append(3)
                remain_moves.remove(3)
                board[0][2] = "X"
                break
            elif move_ai == 4:
                moves_used.append(4)
                remain_moves.remove(4)
                board[1][0] = "X"
                break

            elif move_ai == 6:
                moves_used.append(6)
                remain_moves.remove(6)
                board[1][2] = "X"
                break
            elif move_ai == 7:
                moves_used.append(7)
                remain_moves.remove(7)
                board[2][0] = "X"
                break
            elif move_ai == 8:
                moves_used.append(8)
                remain_moves.remove(8)
                board[2][1] = "X"
                break
            elif move_ai == 9:
                moves_used.append(9)
                remain_moves.remove(9)
                board[2][2] = "X"
                break


#You and the PC choose a move and the number in list "brd" gets replaced
#with a X or O
brd = [[1,2,3],[4,"X",6],[7,8,9]]
#Everytime someone makes a move a number from remain moves list goes to
#move used list and where there are no more numbers in remain_moves
#the game ends
moves_used = []
remain_moves = [1,2,3,4,5,6,7,8,9]
sign_me = "O"
sign_ai = "X"
i = 0
while i <= 4:
    if i == 4:
        print("It is a tie!")
        break
    else:
        if i == 0:
            display_board(brd)
        enter_move(brd)
        display_board(brd)
        man = VictoryFor(brd, sign_me)
        if man == True:
            print("You won!")
            break
        DrawMove(brd)
        print("The AI move was:")
        display_board(brd)
        ai = VictoryFor(brd, sign_ai)
        if ai == True:
            print("AI won!")
            break
        i += 1
