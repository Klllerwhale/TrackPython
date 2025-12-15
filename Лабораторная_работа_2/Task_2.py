salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
poduchik = 0
for i in range(months):
    shortage = spend - salary
    if shortage > 0:
        poduchik += shortage
    spend = spend * (1 + increase)
poduchik = round(poduchik)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", poduchik)
