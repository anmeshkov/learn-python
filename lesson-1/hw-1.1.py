# Задача 1
# Описание:
# Введиет радиус окружности, выведите ее площадь и радиус

import math;
r = input("Введиет радиус окружности в см: ").strip();

try:
  r = float(r)
  if type(r) == float:
    s = round(math.pi * math.pow(r, 2), 2)
    print(f"Площадь окружности: {s}. Радиус: {r} см")
except:
  print("Ошибка требуется ввести число.")

