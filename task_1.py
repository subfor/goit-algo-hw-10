from pulp import LpMaximize, LpProblem, LpStatus, LpVariable, value

# Mодель для максимізації виробництва
model = LpProblem("Максимізація виробництва напоїв", LpMaximize)

# Змінні: кількість одиниць лимонаду (x) і соку (y)
x = LpVariable("Лимонад", lowBound=0, cat="Integer")
y = LpVariable("Фруктовий_сік", lowBound=0, cat="Integer")

# Обмеження на ресурси:
# Вода: 2x + 1y ≤ 100
model += 2 * x + y <= 100, "Обмеження_води"

# Цукор: 1x ≤ 50
model += x <= 50, "Обмеження_цукру"

# Лимонний сік: 1x ≤ 30
model += x <= 30, "Обмеження_лимонного_соку"

# Фруктове пюре: 2y ≤ 40
model += 2 * y <= 40, "Обмеження_пюре"

# Цільова функція — максимізувати кількість вироблених напоїв
model += x + y, "Загальна_кількість_напоїв"

# Розв'язання
model.solve()

print("Статус розв'язку:", LpStatus[model.status])
print("Кількість лимонаду:", x.varValue)
print("Кількість фруктового соку:", y.varValue)
print("Загальна кількість напоїв:", value(model.objective))
