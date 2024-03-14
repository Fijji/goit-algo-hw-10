import pulp

Lemonade = pulp.LpVariable('Лимонад', lowBound=0, cat='Continuous')
Fruit_juice = pulp.LpVariable('Фруктовий_сік', lowBound=0, cat='Continuous')

model = pulp.LpProblem("Оптимізація_виробництва", pulp.LpMaximize)
model += Lemonade + Fruit_juice, "Всього_продуктів"

# Обмеження (constraints)
model += 2 * Lemonade + Fruit_juice <= 100, "Вода"
model += Lemonade <= 50, "Цукор"
model += Lemonade <= 30, "Фруктовий_сік"
model += Fruit_juice <= 40, "Фруктове_пюре"
model += 2 * Lemonade <= 100, "Max_Лимонаду"
model += 2 * Fruit_juice <= 40, "Max_Фруктового_соку"

model.solve()

# Код виконується і повертає максимальну можливу загальну кількість вироблених продуктів "Лимонад" та "Фруктовий сік", враховуючи обмеження на кількість ресурсів.
print(pulp.LpStatus[model.status])
for variable in model.variables():
    print(f"{variable.name} = {variable.varValue}")

print(f"Всього = {pulp.value(model.objective)}")