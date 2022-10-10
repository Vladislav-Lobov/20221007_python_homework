# 0005 Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

a_point_x = float(input('Введите X для точки A: '))
a_point_y = float(input('Введите Y для точки A: '))
b_point_x = float(input('Введите X для точки B: '))
b_point_y = float(input('Введите Y для точки B: '))

distance = ((a_point_x - b_point_x) ** 2 + (a_point_y - b_point_y) ** 2) ** 0.5
print(f'Расстояние между точками A ({a_point_x},{a_point_y}) ')
print(f'и B ({b_point_x},{b_point_y}) равно {distance}')
