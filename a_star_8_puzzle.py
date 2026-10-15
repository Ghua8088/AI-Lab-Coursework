import heapq

start = (("-", "1", "4"), ("8", "2", "3"), ("7", "6", "5"))
goal = (("1", "2", "3"), ("4", "5", "6"), ("7", "8", "-"))

# (row_offset, col_offset): blank moves in this direction, so tile moves in the opposite direction
moves = [
    (0, -1, "right"),  # Blank moves left -> Tile moves right
    (0, 1, "left"),  # Blank moves right -> Tile moves left
    (-1, 0, "down"),  # Blank moves up -> Tile moves down
    (1, 0, "up"),  # Blank moves down -> Tile moves up
]

cache = {}
for i in range(len(goal)):
    for j in range(len(goal[0])):
        cache[goal[i][j]] = (i, j)

def h(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != "-":
                gi, gj = cache[val]
                dist += abs(gi - i) + abs(gj - j)
    return dist

def locate_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == "-":
                return i, j

def get_next_state(state, x, y, nx, ny):
    board = [list(row) for row in state]
    tx, ty = x + nx, y + ny
    board[x][y], board[tx][ty] = board[tx][ty], board[x][y]
    return tuple(tuple(row) for row in board)

def a_star(start, goal):
    open_list = [(h(start), 0, start)]
    g_score = {start: 0}
    parent = {}
    while open_list:
        f, g, current = heapq.heappop(open_list)

        if current == goal:
            actions = []
            curr = goal
            while curr in parent:
                prev_state, action = parent[curr]
                actions.append(action)
                curr = prev_state
            return actions[::-1]

        if g > g_score.get(current, float("inf")):
            continue

        x, y = locate_zero(current)

        for dx, dy, move_dir in moves:
            tx, ty = x + dx, y + dy
            if 0 <= tx < 3 and 0 <= ty < 3:
                tile_moved = current[tx][ty]
                next_state = get_next_state(current, x, y, dx, dy)
                new_g = g + 1

                if new_g < g_score.get(next_state, float("inf")):
                    g_score[next_state] = new_g
                    parent[next_state] = (
                        current,
                        f"Move tile '{tile_moved}' {move_dir}",
                    )
                    heapq.heappush(
                        open_list, (new_g + h(next_state), new_g, next_state)
                    )

    return None
def run(start, goal):
    solution = a_star(start, goal)
    if solution is None:
        print("No solution found.")
        return
    print(f"Solved in {len(solution)} steps:\n")
    for step_num, action in enumerate(solution, 1):
        print(f"{step_num}. {action}")
run(start, goal)