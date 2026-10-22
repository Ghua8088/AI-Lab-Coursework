start = (('1','2','3'),('-','4','6'),('7','5','8'))
target=(('1','2','3'),('4','5','6'),('7','8','-'))
moves=[(0,1),(1,0),(-1,0),(0,-1)]
ROWS=3
COLS=3
def locate_empty(state):
    for i in range(ROWS):
        for j in range(COLS):
            if state[i][j]=='-':
                return (i,j)
def act(state,c,n):
    ci,cj=c
    ni,nj=n
    state=[list(r) for r in state]
    state[ci][cj],state[ni][nj]=state[ni][nj],state[ci][cj]
    return tuple(tuple(r) for r in state)
def dfs(start,target,depth):
    stack=[[start,0]]
    path={}
    while stack:
        curr,curr_depth=stack.pop()
        if curr==target:
            return path
        if curr_depth==depth:
            continue
        ci,cj=locate_empty(curr)
        for di,dj in moves:
            ni,nj=ci+di,cj+dj
            if 0<=ni<ROWS and 0<=nj<COLS:
                new_state=act(curr,(ci,cj),(ni,nj))
                if new_state not in path:
                    stack.append([new_state,curr_depth+1])
                    path[new_state]=curr
    return None
def decode_path(path,start,goal):
    op=[]
    while start!=goal:
        op.append(goal)
        goal=path[goal]
    op.append(goal)
    return op[::-1]
def iddls(start,target,max_depth):
    for depth in range(1,max_depth):
        r=dfs(start,target,depth)
        if r:
            print(decode_path(r,start,target))
            break
iddls(start,target,5)


