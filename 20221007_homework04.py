# 0004 Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

is_not_valid = True

while is_not_valid:
    number = int(input('Введите номер четверти: '))
    if (number < 1) or (number > 4):
        print('Некорректный ввод. Повторите: ')
        is_not_valid = True
    else:
        is_not_valid = False

if number == 1:
    print('Первая четверть: 0 < X < +∞ ; 0 < Y < +∞ ')
elif number == 2:
    print('Вторая четверть: -∞ < X < 0 ; 0 < Y < +∞ ')
elif number == 3:
    print('Третья четверть: -∞ < X < 0 ; -∞ < Y < 0 ')
else:
    print('Четвертая четверть: 0 < X < +∞ ; -∞ < Y < 0 ')
