day = int(input("Введите день: "))
month = int(input("Введите месяц (числом): "))

if 3 <= month <= 5:     # март, апрель, май
    season = "Весна"
elif 6 <= month <= 8:   # июнь, июль, август
    season = "Лето"
elif 9 <= month <= 11:  # сентябрь, октябрь, ноябрь
    season = "Осень"
elif month == 12 or month <= 2:  # декабрь, январь, февраль
    season = "Зима"
else:
    season = "Некорректный месяц"

print(f"Сезон: {season}")