board = [['X','X','.'],['.','.','.'],['.','.','.']]
def move(a,b,x):
    board[a-1][b-1] = x
def firstrow(board):
    if board[0] == ['X','X','X']:
        return 'X'
    if board[0] == ['O','O','O']:
        return 'O'
    return '.'
a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
x = input('Enter X or O: ')
move(a,b,x)
for e in board:
    print(e)
print(firstrow(board))