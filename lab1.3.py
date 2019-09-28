from utils import *

ox = get_dimention('Введите OX: ', 'Ошибка: значение ОХ должно быть больше нуля')
oy = get_dimention('Введите OY: ', 'Ошибка: значение OY должно быть больше нуля')

while True:
    xn = get_coordinate('Введите Xн: ', 'Ошибка: значение Хн должно быть числом')
    xk = get_coordinate('Введите Xк: ', 'Ошибка: значение Хк должно быть числом')
    if xn < xk:
        break
    print('Хн должно быть меньше Хк')

dx = get_dimention('Введите DX: ', 'Ошибка: значение DX должно быть больше нуля')

def polynomial(x):
    return -40 - (-3 * (x + 5)**2) / (2 * x - 6)

if abs(xn) > abs(xk):
    widthx = abs(xn) * ox * 10
else:
    widthx = abs(xk) * ox * 10

widthy = 20 * oy * 10

speed(1)

penup()
goto(-widthx, 0)
pendown()
goto(widthx, 0)

penup()
goto(0, widthy)
pendown()
goto(0, -widthy)

cur_y = oy * 10
cur_x = ox * 10

while cur_x < widthx:
    penup()
    goto(cur_x, 5)
    pendown()
    goto(cur_x, -5)

    penup()
    goto(-cur_x, 5)
    pendown()
    goto(-cur_x, -5)
    penup()

    cur_x += ox * 10

while cur_y < widthy:
    penup()
    goto(-5, cur_y)
    pendown()
    goto(5, cur_y)

    penup()
    goto(-5, -cur_y)
    pendown()
    goto(5, -cur_y)
    penup()

    cur_y += oy * 10


done()