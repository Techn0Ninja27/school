

def array2d(x, y):
    '''creates 2d array with user provided dimensions'''
    array = [[" " for x in range(x)] for y in range(y)]
    return array


def arrayToList(array):
    '''returns list of strings ready to print from game board array'''
    board = []  # opens list to store strings
    for y in range(len(array)):  # goes through y axis of array
        row = ""  # creates string for row
        spacer = ""  # creates string for the spacer between rows
        for x in range(len(array[y])):  # goes through x axis
            # appends value of coordinate in array to string
            row += array[y][x]
            spacer += "-"  # adds to the spacer
            # checks if it is not the last column in the x axis
            if x != (len(array[y]) - 1):
                row += "|"  # adds vertical line to seperate board
                spacer += "+"  # adds cross to spacer for intersection
        board.append(row)  # appends the x axis row to the y axis list
        if y != (len(array) - 1):  # checks if it is not on last row
            board.append(spacer)  # appends spacer to list
    return board  # returns list


def printBoard(board):
    '''prints list of strings organized in an xy coordinate system'''
    for y in range(len(board)):  # iters through y axis
        print(board[y])  # prints rows


def iterableEqual(iterable):
    '''checks if all elements of an iterable are equal and returns boolean'''
    equal = True  # opens variable to check if equal
    for i in iterable:  # iters through iterable
        if i != iterable[0]:  # compares all elements to first element
            equal = False  # if element is different, change equal to false
            break
    return equal  # return boolean


def columnCreator(array, x):
    '''returns column from xy coordinate array'''
    column = []  # opens list to store column
    for y in range(len(array)):  # iters through y axis
        # append appropriate x coordinates to column list
        column.append(array[y][x])
    return column


def winCheck(array):
    "checks for a tic tac toe win"
    xWin = False  # opens boolean for storing x win
    oWin = False  # opens boolean for storing o win
    for y in range(len(array)):  # iters through rows of array
        if iterableEqual(array[y]):  # checks if entire row is equal
            if array[y][0] == "x":  # checks if equal to x
                xWin = True  # sets x win to True
            elif array[y][0] == "o":  # checks if equal to o
                oWin = True  # sets o win to True
            else:
                pass
    for x in range(len(array[0])):  # iters through columns of array
        column = columnCreator(array, x)  # creates list for column
        if iterableEqual(column):  # checks if column is equal
            if column[0] == "x":  # checks if first in column is equal to x
                xWin = True  # sets x win to true
            elif column[0] == "o":  # checks first in column if equal to o
                oWin = True  # set o win to true
            else:
                pass
    if len(array) == len(array[0]):  # checks if array is square
        diag1 = []  # opens list to store first diagonal
        for i in range(len(array)):  # iters array
            diag1.append(array[i][i])  # appends diagonal elements to list
        diag2 = []  # opens list to store second diagonal
        for i in range(len(array)):  # tiers through array
            diag2.append(array[-1-i][i])  # appends diagonal elements to list
    if iterableEqual(diag1):  # checks if diag is equal
        if column[0] == "x":  # checks if first in column is equal to x
            xWin = True  # sets x win to true
        elif column[0] == "o":  # checks first in column if equal to o
            oWin = True  # set o win to true
        else:
            pass
    if iterableEqual(diag2):  # checks if diag is equal
        if column[0] == "x":  # checks if first in column is equal to x
            xWin = True  # sets x win to true
        elif column[0] == "o":  # checks first in column if equal to o
            oWin = True  # set o win to true
        else:
            pass
    if xWin:  # checks for x win
        return "x"
    elif oWin:  # checks for o win
        return "o"
    else:
        return False


def turn(array, player, x, y):
    '''changes element of board'''
    array[y][x] = player  # replaces element at x y coordinate with player
    return array


def illegalCheck(array, x, y):
    '''checks for an illegal move'''
    if array[y][x] == " ":  # checks if specified position is empty
        return True
    else:
        return False


def playerTurn(array, player):
    '''text input for player to make a turn'''
    print("player", player, "turn")
    outOfBounds = True
    while outOfBounds:
        try:
            illegalMove = True  # checks for illegal move
            while illegalMove:  # looped until no illegal move is made
                userError = True  # checks for user error
                while userError:  # looped until no error
                    try:
                        # code run while checking for errors
                        x = int(input("X coordinate"))
                        y = int(input("Y coordinate"))
                    except:
                        # run if error is found
                        print("Enter an Integer")
                        continue
                    else:
                        # if no error, breaks loop
                        userError = False

                if illegalCheck(array, x, y):  # checks for illegal move
                    # if not illegal, makes turn
                    newArray = turn(array, player, x, y)
                    illegalMove = False  # breaks loop
                else:
                    print("illegal move")  # prints illegal move
        except IndexError:
            print("coordinates out of range")
        else:
            outOfBounds = False
    return newArray


def drawCheck(array):
    '''checks for a draw'''
    draw = True
    for y in range(len(array)):
        for x in range(len(array[y])):
            if array[y][x] == " ":
                draw = False
    return draw


def main():
    print("tic tac toe on python")
    print("enter x y coordinate for position of move")
    print("coordinates count from 0, and the y axis is reversed")
    userError = True  # checks for user error
    while userError:  # looped until no error
        try:
            # code run while checking for errors
            print("board size (counts from 0)")  # asks for board size
            boardx = int(input("X length"))
            boardy = int(input("Y length"))
        except:
            # run if error is found
            print("enter integer")
            continue
        else:
            # if no error, breaks loop
            userError = False
    array = array2d(boardx, boardy)  # creates board array
    noWin = True  # checks if there is no win yet
    player = "x"
    while noWin:  # while nobody has won, game loop
        board = arrayToList(array)  # turns array into list for printing
        printBoard(board)  # prints list

        array = playerTurn(array, player)  # turn for player

        if winCheck(array) == ("x" or "o"):  # checks for a win
            noWin = False  # breaks game loop
            board = arrayToList(array)  # prints board
            printBoard(board)
            print("player", player, "has won")

        if drawCheck(array):  # checks for a tie
            noWin = False
            board = arrayToList(array)  # prints board
            printBoard(board)
            print("it is a draw, nobody has won")

        if player == "x":  # if player was x, change to y
            player = "o"
        else:  # vice versa
            player = "x"

    print("game over")


if __name__ == "__main__":
    main()
