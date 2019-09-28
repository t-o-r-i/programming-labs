from turtle import *

def get_dimention(input_string, error_string):
    res = input(input_string)
    if not res.isdigit() or float(res) <= 0:
        print (error_string)
        return get_dimention(input_string, error_string)
    return float(res)

def get_coordinate(input_string, error_string):
    res = input(input_string)
    if not res.lstrip('-').isdigit():
        print (error_string)
        return get_dimention(input_string, error_string)
    return float(res)

x = get_coordinate('Введите X: ', 'Ошибка: значение X должно быть числом')
y = get_coordinate('Введите Y: ', 'Ошибка: значение Y должно быть числом')
w = get_dimention('Введите W: ', 'Ошибка: значение ширины должно быть больше нуля')
h = get_dimention('Введите H: ', 'Ошибка: значение высоты должно быть больше нуля')

interval = (w / 17)

def move(z, t):
    position = {
    'x': x + interval * z,
    'y': y + h * t
    }
    goto(position['x'], position['y'])

penup()
move(0, 0)
move(- 8.5, - 0.5)
pendown()
move(- 8.5, 0.5)
move(- 6.5, 0.5)
move(- 6.5, - 0.5)
penup()

move(- 5.5, 0)
pendown()
move(- 3.5, 0)
move(- 3.5, - 0.5)
move(- 5.5, - 0.5)
move(- 5.5, 0.5)
move(- 4.25, 0.5)
move(- 4.25, 0)
penup()

move(- 2.5, - 0.5)
pendown()
move(- 2.5, 0.5)
move(- 0.5, 0.5)
penup()

move(0.5, 0.5)
pendown()
move(2.5, 0.5)
move(2.5, 0)
move(0.5, 0)
move(0.5, - 0.5)
move(2.5, - 0.5)
penup()

move(3.5, 0)
pendown()
move(4.5, 0.5)
move(4.5, - 0.5)
move(3.5, - 0.5)
move(5.5, - 0.5)
penup()

move(8.5, 0.5)
pendown()
move(6.5, 0.5)
move(6.5, 0)
move(8.5, 0)
move(8.5, - 0.5)
move(6.5, - 0.5)

done()