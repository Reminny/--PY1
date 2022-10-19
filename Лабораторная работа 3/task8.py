money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
total = money_capital + salary
while True:
    total -= spend
    spend *= 1 + increase
    month += 1
    if total < spend:
        break
    total += salary
print(month)
