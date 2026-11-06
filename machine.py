# ЗАДАЧА 1
print("ЗАДАЧА 1. Один крок для однієї машини")

x = 0.97
y = 8.7
w = 5
lr = 0.1

prediction = w * x
error = (prediction - y) ** 2
gradient = 2 * (prediction - y) * x

new_w = w - lr * gradient
new_prediction = new_w * x
new_error = (new_prediction - y) ** 2

print("Початковий прогноз:", prediction)
print("Початкова помилка:", error)
print("Крутизна:", gradient)
print("Нова вага:", new_w)
print("Новий прогноз:", new_prediction)
print("Нова помилка:", new_error)
print("Стало краще:", new_error < error)


# ЗАДАЧА 2
print("\nЗАДАЧА 2. Чи згодні машини?")

cars = [
    ("Fiat 128", 0.85, 8.1),
    ("Pontiac Catalina", 2.01, 16.8)
]

for w in [5, 9]:
    print("\nВага w =", w)

    for name, x, y in cars:
        gradient = 2 * (w * x - y) * x
        print(name, "Крутизна:", round(gradient, 4))

        if gradient < 0:
            print("Потрібно збільшувати w")
        elif gradient > 0:
            print("Потрібно зменшувати w")
        else:
            print("Змінювати w не потрібно")


# ЗАДАЧА 3
print("\nЗАДАЧА 3. Розмір кроку")

for lr in [0.1, 0.5, 0.9, 1.0, 1.1]:
    w = 12
    print("\nlr =", lr)

    for step in range(5):
        error = (w - 8) ** 2
        print("Крок:", step,
              "w:", round(w, 4),
              "Помилка:", round(error, 4))

        gradient = 2 * (w - 8)
        w = w - lr * gradient

print("\nВисновок: при lr < 1 помилка зменшується.")
print("При lr = 1 помилка не змінюється.")
print("При lr > 1 помилка зростає.")


# ЗАДАЧА 4
print("\nЗАДАЧА 4. Backprop")

x = 1
y = 6
w1 = 2
w2 = 2
lr = 0.05

h = x * w1
prediction = h * w2
error = (prediction - y) ** 2

d_prediction = 2 * (prediction - y)
gradient_w2 = d_prediction * h
d_h = d_prediction * w2
gradient_w1 = d_h * x

print("h:", h)
print("Прогноз:", prediction)
print("Помилка:", error)
print("Вплив прогнозу:", d_prediction)
print("Крутизна w2:", gradient_w2)
print("Вплив h:", d_h)
print("Крутизна w1:", gradient_w1)

# Перевірка градієнтів
delta = 0.001

error_w1 = (x * (w1 + delta) * w2 - y) ** 2
check_w1 = (error_w1 - error) / delta

error_w2 = (x * w1 * (w2 + delta) - y) ** 2
check_w2 = (error_w2 - error) / delta

print("Перевірка w1:", check_w1)
print("Перевірка w2:", check_w2)

# Один крок навчання
w1 = w1 - lr * gradient_w1
w2 = w2 - lr * gradient_w2

new_prediction = x * w1 * w2
new_error = (new_prediction - y) ** 2

print("Нова w1:", w1)
print("Нова w2:", w2)
print("Новий прогноз:", new_prediction)
print("Нова помилка:", new_error)
print("Помилка зменшилась:", new_error < error)


# ЗАДАЧА 5
print("\nЗАДАЧА 5. Нульові ваги")

x = 1
y = 6
w1 = 0
w2 = 0

h = x * w1
prediction = h * w2
error = (prediction - y) ** 2

gradient_w2 = 2 * (prediction - y) * h
gradient_w1 = 2 * (prediction - y) * w2 * x

print("Прогноз:", prediction)
print("Помилка:", error)
print("Крутизна w1:", gradient_w1)
print("Крутизна w2:", gradient_w2)

print("Навчання не відбувається,")
print("тому що обидві крутизни дорівнюють нулю.")
print("Випадкові початкові ваги допомагають")
print("уникати симетрії між нейронами.")
