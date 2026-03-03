n = int(input("Enter board size (N): "))

board = [" " for _ in range(n * n)]
quen_pos = []


def draw_board(n, board):
    for row in range(n):
        print("+---" * n + "+")
        for col in range(n):
            index = row * n + col
            print("|", board[index], end=" ")
        print("|")
    print("+---" * n + "+\n")


def is_valid(positions):
    row = set()
    col = set()
    dia1 = set()
    dia2 = set()

    for r, c in positions:
        if r in row:
            return False, "Same Row Detected"

        if c in col:
            return False, "Same Column Detected"

        if (r - c) in dia1:
            return False, "Diagonal not allowed"

        if (r + c) in dia2:
            return False, "Anti Diagonal also not allowed"

        row.add(r)
        col.add(c)
        dia1.add(r - c)
        dia2.add(r + c)

    return True, "Abhi tk to theeq ha"


print(f"Enter {n} cell numbers (1 to {n*n}) to place {n} queens.")

draw_board(n, board)

i = 0
while i < n:
    try:
        cell_no = int(input(f"Queen {i+1} - Cell number: "))
    except ValueError:
        print("Only Numbers are allowed")
        continue

    if not (1 <= cell_no <= n * n):
        print("Invalid cell number. Try again.\n")
        continue

    index = cell_no - 1

    if board[index] == "Q":
        print("Placement error \n")
        continue

    board[index] = "Q"

    row = index // n
    col = index % n
    quen_pos.append((row, col))

    draw_board(n, board)

    ok, msg = is_valid(quen_pos)
    print("Status:", msg)

    if not ok:
        print("Invalid placement , Program ended.")
        break

    i += 1

else:
    final_ok, final_msg = is_valid(quen_pos)
    if final_ok and len(quen_pos) == n:
        print("Final Result: All Queens are placed well.")
    else:
        print("Final Result:", final_msg)