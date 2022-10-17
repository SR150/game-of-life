xSize=30
ySize=30
squareSize=20
time=1000#time between generations
initialCells=[[15,15],[14,16],[15,16],[16,16],[14,17]]#initial live cell coodinates
wrapAround=False
import tkinter
root=tkinter.Tk()#setup screen
root.geometry(str(xSize*squareSize)+'x'+str(ySize*squareSize))
canvas = tkinter.Canvas(root, width=xSize*squareSize, height=xSize*squareSize)
canvas.pack()
canvas.configure(background='black')


board=[]
squares=[]#holds shapes making up board on screen
for x in range (xSize):
    board.append([])
    for y in range (ySize):
        board[-1].append(False)

def getCell(board,x,y):
    if x>=len(board):
        if wrapAround:
            return getCell(board,x-len(board),y)
        return False
    if y>=len(board[0]):
        if wrapAround:
            return getCell(board,x,y-len(board[0]))
        return False
    return board[x][y]

def update():#generates new generation
    global board
    toChange=[]#list that stores the squares that need to change state
    
    for x in range(xSize):
        for y in range(ySize):
            alive=0#count all squares adjacent that are alive
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if getCell(board,x+dx,y+dy) and not(dx==0==dy):
                        alive+=1


            #check if it changes state
            if board[x][y]:
                if not ( alive==2 or alive==3):
                    toChange.append([x,y])

            if not board[x][y] and alive==3:
                toChange.append([x,y])
    
    #go through to Change and update all squares in it
    updateBoard(toChange)
    
    root.after(time,update)

def showBoard():
    global squareSize
    global squares
    global board
    for x in range(len(board)):
        squares.append([])
        for y in range(len(board[0])):
            if board[x][y]:
                squares[x].append(canvas.create_rectangle(squareSize*x,
                                                           squareSize*y,
                                                           squareSize*(x+1),
                                                           squareSize*(y+1),
                                                           fill='white'))
            else:
                squares[-1].append('')


           
def updateBoard(toChange):
    global squares
    global board
    global canvas
    for i in toChange:
        x=i[0]
        y=i[1]
        board[x][y]=not board[x][y]
        if board[x][y]:
            squares[x][y]=canvas.create_rectangle(squareSize*x,
                                                       squareSize*y,
                                                       squareSize*(x+1),
                                                       squareSize*(y+1),
                                                       fill='white')
        if not board[x][y]:
            canvas.delete(squares[x][y])

showBoard()
updateBoard(initialCells)
root.after(time,update)
root.mainloop()
