#1
marks = {
    "Анна": 5,
    "Иван": 3,
    "Олег": 4
}

print(marks["Иван"])

marks.update({"Иван": 4, "Мария": 5})

marks.pop("Олег")

print(len(marks))
print(*[f"{name}: {score}"for name, score in marks.items()])

#2

phones = {
    "Анна": "+7 900 111-11-11",
    "Иван": "+7 900 222-22-22",
    "Олег": "+7 900 333-33-33"
}

name = input("имя: ")

if name in phones:
    print(f"Номер: {phones[name]}")
else:
    print("Контакт не найден")
    phones[name] = input("номер: ")

print("\nТелефонная книга:")
print(*[f"{k}: {v}" for k, v in phones.items()], sep="\n")