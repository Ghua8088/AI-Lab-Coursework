start=(("-","1","4"),("8","2","3"),("7","6","5"))
goal=(("1","2","3"),("4","5","6"),("7","8","-"))
possible=[(0,-1),(-1,0),(1,0),(0,1)]
direction=["right","down","up","left"]
def locate_zero(start):
    for i in range(len(start)):
        for j in range(len(start[i])):
            if start[i][j]=="-":
                return i,j
def next_start(start,x,y,nx,ny):
    board = [list(row) for row in start]
    tx, ty = x + nx, y + ny
    board[x][y], board[tx][ty] = board[tx][ty], board[x][y]
    return tuple(tuple(row) for row in board)
def ID_DLS(start,goal,l,seen):
    if start==goal:
        return ["success"]
    if l==0:
        return None
    x,y=locate_zero(start)
    seen.add(start)
    for nx,ny in possible:
        if 0<=x+nx<3 and 0<=y+ny<3:
            new_start=next_start(start,x,y,nx,ny)
            if new_start not in seen:
                path=ID_DLS(new_start,goal,l-1,seen)
                if path:
                    return ["move "+ start[x+nx][y+ny] +" "+ direction[possible.index((nx,ny))]]+path
    seen.remove(start)
    return None
def run(start,goal):
    while True:
        for l in range(100):
            path=ID_DLS(start,goal,l,set())
            if path:
                for i in path:
                    print(i)
                print(f"Path found at depth {l}")
                return
            print(f"Level {l} not possible")
run(start,goal)
    

