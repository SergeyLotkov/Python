
weight = 75 # Вес

height = 175 # Рост

steps = 84600 # Количество пройденных за день шагов

hours = 2 # Время движения в часах

len_step_m = 0.65 # Длина одного шага в метрах

transfer_coeff = 1000 # Коэффициент перевода значения расстояния из метров в километры
dist =  (steps * len_step_m) / transfer_coeff # Напишите формулу расчёта

mean_speed = dist / hours

minutes = hours * 60

spent_calories = (0.035*weight + (mean_speed**2 / height) * 0.029*weight) * minutes

output = f'Сегодня вы прошли {dist:.2f} км и затратили {spent_calories:.2f} каллорий' # Здесь подготовьте строку для вывода

if dist >= 6.5:
    print('Отличный результат! Цель достигнута.')
elif dist >= 3.9:
    print('Неплохо! День был продуктивным')
elif dist >= 2:
    print('Маловато, но завтра наверстаем!')
else:
    print('Лежать тоже полезно. Главное-участие, а не победа!') 


print(output)