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

name = input("\nимя: ")

if name in phones:
    print(f"Номер: {phones[name]}")
else:
    print("Контакт не найден")
    phones[name] = input("номер: ")

print("\nТелефонная книга:")
print(*[f"{k}: {v}" for k, v in phones.items()], sep="\n")

#3
prices = {
    "хлеб": 50,
    "молоко": 90,
    "сыр": 150,
    "яблоко": 30
}


product = input("\nназвание товара: ")
quantity = int(input("количество: "))


if product in prices:
    total_cost = prices[product] * quantity
    print(f"Стоимость: {total_cost} ")
else:
    print("Товар не найден")


print("\nТовары до 100: ")
for name, price in prices.items():
    if price <= 100:
        print(f"{name}: {price} руб.")


#4 

marks = {
    "Анна": 5,
    "Иван": 3,
    "Олег": 4,
    "Мария": 5,
    "Пётр": 2
}


if not marks:
    print("\nНет данных")
else:
    
    average = sum(marks.values()) / len(marks)
    print(f"\nСредняя оценка группы: {average:.2f}")

    print("оценка 5:", *[name for name, mark in marks.items() if mark == 5])
   
    low_marks_count = sum(1 for mark in marks.values() if mark < 4)
    print(f" Оценка ниже 4: {low_marks_count}")

    high_marks = {name: mark for name, mark in marks.items() if mark >= 4}
    print("Оценка не ниже 4:", high_marks)


#5

text = input("\nтекст: ").lower()
words = text.split()
word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

for word, count in word_counts.items():
    print(f"{word}: {count}")


#7

journal = {
    "Анна": [5, 4, 5],
    "Иван": [3, 4, 3],
    "Олег": [4, 5, 4],
    "Мария": []
}

averages = {}


for name, marks in journal.items():
    if marks:  
        averages[name] = sum(marks) / len(marks)
    else:
      
        print(f"\n{name}: нет оценок")


print("\n средний балл >= 4:")
for name, avg in averages.items():
    if avg >= 4:
        print(f"{name}: {avg:.2f}")


if averages:
    max_avg = max(averages.values())
    best_marks = [name for name, avg in averages.items() if avg == max_avg]
    print(f"\n(средний балл {max_avg:.2f}):", ", ".join(best_marks))
else:
    print("Нет данных")

#8

student = {
    "id": 101,
    "name": "Анна",
    "age": 18,
    "is_active": True,
    "marks": [5, 4, 5, 4],
    "address": {
        "city": "Москва",
        "street": "Лесная"
    },
    "phone": None
}


print(f"\nИмя: {student['name']}, Возраст: {student['age']}, Город: {student['address']['city']}")


student["marks"].append(5)


student["average"] = sum(student["marks"]) / len(student["marks"])


student["address"]["city"] = "Казань"


student["phone"] = input("Введите номер телефона: ")


student["has_scholarship"] = student["is_active"] and student["average"] >= 4.5


print("\n--- Карточка студента ---")
for key, value in student.items():
    print(f"{key}: {value}")

#9

product = {
    "id": 42,
    "title": "Наушники",
    "price": 3500,
    "in_stock": True,
    "tags": ["техника", "звук"],
    "specs": {
        "wireless": True,
        "battery_hours": 30,
        "color": "чёрный"
    },
    "reviews": [
        {"author": "Иван", "rating": 5, "text": "Хороший звук"},
        {"author": "Ольга", "rating": 4, "text": "Удобные"}
    ]
}


print(f"\nНазвание: {product['title']}, Цена: {product['price']}, Цвет: {product['specs']['color']}, Время работы: {product['specs']['battery_hours']} ч.")


product["price"] = product["price"] * 0.9


if "скидка" not in product["tags"]:
    product["tags"].append("скидка")


product["reviews"].append({"author": "Анна", "rating": 3, "text": "Быстро разряжаются"})


total_rating = sum(review["rating"] for review in product["reviews"])
product["rating"] = total_rating / len(product["reviews"])


print("оценка ниже 4:", *[r["author"] for r in product["reviews"] if r["rating"] < 4])


if product["in_stock"] and product["specs"]["wireless"]:
    print("Можно заказать")
else:
    print("Не подходит")

#10

order = {
    "number": "A-102",
    "customer": {
        "name": "Максим",
        "email": "max@example.com"
    },
    "items": [
        {"title": "Тетрадь", "price": 80, "quantity": 3},
        {"title": "Ручка", "price": 50, "quantity": 2}
    ],
    "delivery": {
        "method": "курьер",
        "price": 200
    },
    "paid": False,
    "comment": None
}


print(f"Заказ {order['number']} для {order['customer']['name']}")



print("\nПозиции:")
total_items_cost = 0
for item in order["items"]:
    cost = item["price"] * item["quantity"]
    total_items_cost += cost
    print(f"- {item['title']}: {item['quantity']} шт. x {item['price']} руб. = {cost} руб.")


print(f"Стоимость: {total_items_cost} руб.")


if total_items_cost >= 1000:
    order["delivery"]["price"] = 0


order["total"] = total_items_cost + order["delivery"]["price"]
print(f"Итого: {order['total']} руб.")


print("Заказ оплачен" if order["paid"] else "Ожидает оплаты")


if order["comment"] is None:
    print("Комментария нет")
else:
    print(f"Комментарий: {order['comment']}")