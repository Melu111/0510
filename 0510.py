print("это калькулятор")
print("Введите число...........")
print()

result = None

while True:
    line = input()

    if line == "=":
        print(result)
        break

    if line in ("+", "-", "*", "/"):
        op = line
        continue

    number = float(line)

    if result is None:
        result = number
    else:
        if op == "+":
            result = result + number
        elif op == "-":
            result = result - number
        elif op == "*":
            result = result * number
        elif op == "/":
            result = result / number
