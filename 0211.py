names = [" Петя", "Вася", "Таня"]
marks = [5, 3, 4]
tu = (2, 3)


bad_table = [["Петя", 5],["Вася", 3],["Таня", 4]]

table = {"Петя":5, "Вася": 3, "Таня": 4,}


print(table)

table["Костя"] = 2
print(table.get("Костя", 0))
print(table.get("Петя", 0))
#del table ["Вася"]

#print(table.pop("Вася", 0))
print (table)
for i in table:
    print("Студент", i)
    print("Оценка", table[i])

a = list(table.keys())
b = table.values()
c = table.items()

for name, mark in c:
    print(name)
    print(mark)

