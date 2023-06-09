def set_board(g):
    print("---------")
    for ln in range(3):
        print(f"| {g[ln * 3]} {g[ln * 3 + 1]} {g[ln * 3 + 2]} |")
    print("---------")


def get_game_state(g):
    rows = ["".join([g[a * 3 + b] for b in range(3)]) for a in range(3)]
    cols = ["".join([g[a + b * 3] for b in range(3)]) for a in range(3)]
    diag = [g[0] + g[4] + g[8], g[2] + g[4] + g[6]]

    three_x_count = rows.count("XXX") + cols.count("XXX") + diag.count("XXX")
    three_o_count = rows.count("OOO") + cols.count("OOO") + diag.count("OOO")

    no_of_x = g.count("X")
    no_of_o = g.count("O")

    if abs(no_of_x - no_of_o) > 1 or three_x_count + three_o_count > 1:
        return "Impossible"
    if three_o_count == three_x_count == 0:
        if no_of_x + no_of_o < 9:
            return "Continue"
        else:
            return "Draw"
    if three_x_count == 1:
        return "X wins"
    if three_o_count == 1:
        return "O wins"


def make_step(g, player):
    while True:
        user_input = input().split(" ")
        try:
            x = int(user_input[0])
            y = int(user_input[1])
        except ValueError:
            print("You should enter numbers!")
            continue
        if x not in range(1, 4) or y not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
            continue
        if g[y - 1 + (x - 1) * 3] != " ":
            print("This cell is occupied! Choose another one!")
            continue
        else:
            g[y - 1 + (x - 1) * 3] = player
            break


symbols = list("         ")
players = ["X", "O"]
counter = 0
set_board(symbols)
while True:
    player = players[counter % 2]
    counter += 1
    make_step(symbols, player)
    set_board(symbols)
    status = get_game_state(symbols)
    if status != "Continue":
        print(status)
        break

