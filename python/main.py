#1 сортировка чисел по возрастанию
a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print(a + b + c - min(a, b, c) - max(a, b, c))
print(min(a, b, c))

#2 Корни уравнения
# объявление функции
def solve(a, b, c):
    d = (b ** 2) - 4 * a * c
    x1 = ((-1 * b) - d ** 0.5) / (2 * a)
    x2 = ((-1 * b) + d ** 0.5) / (2 * a)
    return min(x1, x2), max(x1, x2)
# считываем данные
a, b, c = int(input()), int(input()), int(input())
# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
#3 Формула получения красилого чилса (число %7 или 17)
a = int(input())
if (a%7 == 0 or a % 17 == 0) and(a >= 1000 and a <= 9999):
    print('YES')
else:
    print('NO')