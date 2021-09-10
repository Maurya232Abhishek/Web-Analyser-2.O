horseSet=set()
bishopSet=set()
def isPosValid(y,x):
    if x<1 or x>8 or y<1 or y>8:
        return False
    t=(y,x)
    if t in horseSet:
        return False
    return True
def getRow():
    l=list(range(9))
    for i in range(9):
        l[i]=0
    return l
def getBoard():
    l=[]
    for i in range(9):
        l= l + [getRow()]
    return l
def printBoard(board):
    for y in range(1,9):
        print(board[y][1:])
def OneHorseMove(board,y,x):
    newx = x + 1
    newy = y + 2
    t=(newy,newx)
    if isPosValid(newy,newx):
        if not t in horseSet:
            board[newy][newx]=1
            horseSet.add(t)
    newx = x + 1
    newy = y - 2
    t=(newy,newx)
    if isPosValid(newy, newx):
        if not t in horseSet:
            board[newy][newx]=1
            horseSet.add(t)
    newx = x + 2
    newy = y + 1
    t=(newy,newx)
    if isPosValid(newy, newx):
        if not t in horseSet:
            board[newy][newx]=1
            horseSet.add(t)
    newx = x + 2
    newy = y - 1
    t=(newy,newx)
    if isPosValid(newy, newx):
        if not t in horseSet:
            board[newy][newx]=1
            horseSet.add(t)

    newx = x - 1
    newy = y + 2
    t=(newy,newx)
    if isPosValid(newy,newx):
        if not t in horseSet:
            board[newy][newx]=1
            horseSet.add(t)
    newx = x - 1
    newy = y - 2
    t=(newy,newx)
    if isPosValid(newy, newx):
        if not t in horseSet:
            board[newy][newx]=1
            horseSet.add(t)
    newx = x - 2
    newy = y + 1
    t=(newy,newx)
    if isPosValid(newy, newx):
        if not t in horseSet:
            board[newy][newx]=1
            horseSet.add(t)
    newx = x - 2
    newy = y - 1
    t=(newy,newx)
    if isPosValid(newy, newx):
        if not t in horseSet:
            board[newy][newx]=1
            horseSet.add(t)

def OneBishopMove(board,y,x):
    # x+y x-y
    c1=x+y
    c2=x-y
    x1=x2=x
    y1=y2=y
    while isPosValid(y1,x1):
        board[y1][x1]=1
        t=(y1,x1)
        bishopSet.add(t)
        x1 += 1
        y1 -= 1
    x1 = x2 = x
    y1 = y2 = y
    while isPosValid(y1,x1):
        board[y1][x1] = 1
        t=(y1,x1)
        bishopSet.add(t)
        x1 -= 1
        y1 +=1
    x1 = x2 = x
    y1 = y2 = y
    while isPosValid(y2,x2):
        board[y2][x2] = 1
        t=(y2,x2)
        bishopSet.add(t)
        x2 += 1
        y2 += 1#x1 - c2
    x1 = x2 = x
    y1 = y2 = y
    while isPosValid(y2, x2):
        board[y2][x2] = 1
        t = (y2, x2)
        bishopSet.add(t)
        x2 -= 1
        y2 -= 1# x1 - c2

b=getBoard()
#printBoard(b)
b[1][1]=1

horseSet.add((1,1))
for i in range(6):
    copyset=horseSet.copy()
    for s in copyset:
        y=s[0]
        x=s[1]
        OneHorseMove(b,y,x)
print(horseSet)
printBoard(b)

b2=getBoard()
b2[1][1]=1
bishopSet.add((1,1))
for i in range(3):
    copyset=bishopSet.copy()
    for s in copyset:
        y=s[0]
        x=s[1]
        OneBishopMove(b2,y,x)
print(bishopSet)
printBoard(b2)