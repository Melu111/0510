field = [
    ["", "", "",],
    ["", "", "",],
    ["", "", "",],
]
x_turn = True
turns_made = 0

def print_field():
    global field

    for i in field: #i - строка
        for j in i:
            if j == "":
                j = "_"
            print(j, end="")
            print() # end = "\n"
def get_coords(name: str) -> list[int]:
    correct +["1", "2", "3"]
    print("Ход" + name + ". Введите номер строки (1, 2, 3): ")
    x = int(input("> "))


def turn(x_turn: bool) -> None:
    global field
    correct = ["1", "2", "3"]
    if  x_turn:
        name = "крестиков"
        sym = "x"
    else:
        name = "ноликов"
        sym = "0"
    x, y = get_coords(name)
    while field[x][y] != "":
        print("Ошибка - клетка занята" + field[x][y])

        x, y =get_coords (name)
    field[x][y] = sym


    while x not in correct:
        print("Некорректно. Введите номер строки (1, 2, 3):")
    print("Введите номер столбца (1, 2, 3): ")
    y = int(input("> "))
    while y not in correct:
        print("Некорректно. Введите номер столбца (1, 2, 3):")
        x = int(x)-1
        y = int(y)-1
        return [x, y]

def check_win() -> str:
    global field

    out = ""
    for i in range(3):
        xs = field[i][0] #первый символ строки
        ys = field[0][i] #первый символ столбца
        xwin, ywin = True, True
        for j in range(3):
            if field[i][j] != xs:
                xwin = False
            if field[j][i] != ys:
                ywin = False
        if xwin and out =="":
            out = xs
        if ywin and out == "":
            out = ys
    xs = field[0][0]
    ys = field [0][2]
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
    return out
while True:
    print_field()
    turn(x_turn)
    x_turn = not x_turn
    turns_made += 1
    if turns_made >= 9:
        print("ничья")
    elif result == "X":
        print("победа крестиков")
    else:
        print("победа ноликов")
    turns_made +=1
    if turns_made >=9:
        pass



