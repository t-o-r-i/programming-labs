from utils import *

x = get_coordinate('Введите X: ', 'Ошибка: значение X должно быть числом')
y = get_coordinate('Введите Y: ', 'Ошибка: значение Y должно быть числом')
w = get_dimention('Введите W: ', 'Ошибка: значение ширины должно быть больше нуля')
h = get_dimention('Введите H: ', 'Ошибка: значение высоты должно быть больше нуля')

interval = (w / 17)

def move_interval(z, t):
    position = {
    'x': x + interval * z,
    'y': y + h * t
    }
    goto(position['x'], position['y'])

penup()
move_interval(0, 0)
move_interval(- 8.5, - 0.5)
pendown()
move_interval(- 8.5, 0.5)
move_interval(- 6.5, 0.5)
move_interval(- 6.5, - 0.5)
penup()

move_interval(- 5.5, 0)
pendown()
move_interval(- 3.5, 0)
move_interval(- 3.5, - 0.5)
move_interval(- 5.5, - 0.5)
move_interval(- 5.5, 0.5)
move_interval(- 4.25, 0.5)
move_interval(- 4.25, 0)
penup()

move_interval(- 2.5, - 0.5)
pendown()
move_interval(- 2.5, 0.5)
move_interval(- 0.5, 0.5)
penup()

move_interval(0.5, 0.5)
pendown()
move_interval(2.5, 0.5)
move_interval(2.5, 0)
move_interval(0.5, 0)
move_interval(0.5, - 0.5)
move_interval(2.5, - 0.5)
penup()

move_interval(3.5, 0)
pendown()
move_interval(4.5, 0.5)
move_interval(4.5, - 0.5)
move_interval(3.5, - 0.5)
move_interval(5.5, - 0.5)
penup()

move_interval(8.5, 0.5)
pendown()
move_interval(6.5, 0.5)
move_interval(6.5, 0)
move_interval(8.5, 0)
move_interval(8.5, - 0.5)
move_interval(6.5, - 0.5)

done()