d=5


field = []
for i in range(d):
    field.append([""]*d)
x_turn = True
turns_made = 0

x_Turn = True
turns_made = 0
def print_field():
    global field

    for i in field:
        for j in i:
            if j == "":
                j = "_"
            print(j, end="")
        print()

def get_coords(name: str) -> list[int]:
    correct = ["1", "2", "3"]
    print("ход" + name + ". введите номер строки (1, 2, 3):")
def turn(x_turn: bool) -> None:
    global field
    correct = ["1", "2", "3"]
    if x_turn:
        name = "крестиков"
        sym = "x"
    else:
        name = "ноликов"
        sym = "0"
        x, y =get_coords (name)
    while field[x][y] != "":
        print("ошибка - клетка занята" + field[x][y])
        x, y =get_coords (name)
    field[x][y] = sym

    print("ход" + name + ". введите номер строки (1, 2, 3):")
    x = int(input("> "))
    while x not in correct:
        print("Некорректно. введите номер строки (1, 2, 3):")
    print("введите номер столбца(1, 2, 3):")
    y = int(input("> "))
    while y not in correct:
        print("Некорректно. введите номер столбца (1, 2, 3):")
        x = int(x)-1
        y = int(y)-1
        return[x, y]

def check_win() -> str:
    global field

    out = ""
    for i in range(3):
        xs = field[i][0]
        ys = field[0][i]
        xwin, ywin = True, True
        for j in range(3):
            if field[i][j] != xs:
                xwin = False
            if field[j][i] != ys:
                ywin = False
        if xwin and out == "":
            out = xs
        if ywin and out == "":
            out = ys
    xs = field[0][0]
    ys = field[0][2]
    xwin, ywin = True, True
    for i in range(3):
        if field[i][i] != xs:
            xwin = False
            if field[i][2-i] != ys:
                ywin = False
    if xwin and out == "":
        out = xs
    if ywin and out == "":
        out = ys
        return out

def reset() -> None:
    global field, x_turn, turns_made
    print("Хотите продолжить? [да/нет]")
    s = input("> ")
    if s == "нет":
        raise SystemExit



while True:
    print_field()
    turn(x_turn)
    x_turn = not x_turn
    turns_made +=1
    result = check_win()
    if result == "":
        if turns_made >= 9:
            print("ничья")
            reset()
    elif result == "X":
        print("победа крестиков")
        reset()
    else:
        print("победа ноликов")
        reset()
    turns_made +=1
