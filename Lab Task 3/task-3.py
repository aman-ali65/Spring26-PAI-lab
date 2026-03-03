

def water_jug_dfs(x_cap,y_cap,gol):

    def is_goal(state):
        x, y = state
        return x == gol or y == gol

    def successors(state):
        x, y = state
        succ = []

        if x < x_cap:
            succ.append((1, (x_cap, y)))

        if y < y_cap:
            succ.append((2, (x, y_cap)))

        if x > 0:
            succ.append((3, (0, y)))

        if y > 0:
            succ.append((4, (x, 0)))

        if x > 0:
            total = x + y
            new_y = total
            if new_y > y_cap:
                new_y = y_cap
            succ.append((5, (0, new_y)))

        if x > 0 and y < y_cap:
            space = y_cap - y
            transfer = x
            if transfer > space:
                transfer = space
            succ.append((6, (x - transfer, y + transfer)))

        if y > 0:
            total = x + y
            new_x = total
            if new_x > x_cap:
                new_x = x_cap
            succ.append((7, (new_x, 0)))

        if y > 0 and x < x_cap:
            space = x_cap - x
            transfer = y
            if transfer > space:
                transfer = space
            succ.append((8, (x + transfer, y - transfer)))

        return succ

    def dfs(start):
        visited = set()
        path = [(0, start)]

        def rec(state):
            if is_goal(state):
                return True

            visited.add(state)

            for rule_no, nxt in successors(state):
                if nxt in visited:
                    continue
                path.append((rule_no, nxt))
                if rec(nxt):
                    return True
                path.pop()

            return False

        if rec(start):
            return path
        return None


    start_state = (0, 0)
    result = dfs(start_state)

    if result is None:
        print("No solution found.")
    else:
        print("DFS Solution Found!\n")
        print("Start State:", result[0][1])

        for i in range(1, len(result)):
            rule_no, state = result[i]
            print("Rule", rule_no)
            print("       ->  New State =", state)

        print("\nGOAL reached at:", result[-1][1])



x_cap = 7
y_cap = 4
gol  = 5

water_jug_dfs(x_cap=7,y_cap=4,gol=5)