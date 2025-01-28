# Задача 2
# Описание:
# Считайте два числа, выведите их произведение, если оно больше 1000, вместо этого выведите их сумму.

num_1 = input('Введите число первое число: ').strip()
num_2 = input('Введите второе первое число: ').strip()

def NumberOperation(num1, num2):
  num1 = float(num1)
  num2 = float(num2)
  print(f"Произведение чисел {num1} {num2} равно {num1 * num2}") if num1 * num2 >= 1000 else print(f"Сумма чисел {num1} {num2} равна {num1 + num2}")


NumberOperation(num_1, num_2)