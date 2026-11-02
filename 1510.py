import math

acc = 0
init = False
while True:
    inp = input()
    if inp == "exit":
        break
    elif inp == "C":
        acc = 0
        init = False
        sign = ""
    elif  inp == "+":
        sign = "+"
    elif inp == "-":
        sign = "-"
    elif inp == "/":
        sign = "/"
    elif inp == "*":
        sign = "*"
    elif inp == "**":
        sign = "**"
    elif  inp == "sin":
        acc = math.sin(acc)
    elif inp == "cos":
        acc = math.cos(acc)
    else:
        inp = float(inp)
        if sign == "":
            acc = inp
        else:
            acc = eval (str(acc)+sign+str(inp))
            sign = ""