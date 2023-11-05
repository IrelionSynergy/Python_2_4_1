print('Введите стороны прямоугольника')
side_1 = float(input())
side_2 = float(input())
perimeter = (side_1 + side_2) * 2
square = side_1 * side_2
print('Результат:')
print('Периметр прямоугольника равен: {p}'.format(p=perimeter))
print('Площадь прямоугольника равена: {s}'.format(s=square))