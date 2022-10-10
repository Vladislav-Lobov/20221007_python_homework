# 0002 Напишите программу для проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


numbers = [[0, 0, 0],
           [0, 0, 1],
           [0, 1, 0],
           [0, 1, 1],
           [1, 0, 0],
           [1, 0, 1],
           [1, 1, 0],
           [1, 1, 1]]

count = 0  # счетчик ложных утверждений
for i in range(8):
    x = numbers[i][0]
    y = numbers[i][1]
    z = numbers[i][2]
    print(f'X={x} Y={y} Z={z}')
    left = not (x or y or z)
    print(f'выражение ¬({x} ⋁ {y} ⋁ {z}) равно {left}')
    right = (not x) and (not y) and (not z)
    print(f'выражение ¬{x} ⋀ ¬{y} ⋀ ¬{z} равно {right}')
    if left != right:
        count = count + 1

if count == 0:
    print('выражение верно для всех значений предикат')
