'''
Title 
Group:
Sineokaya Anastasia
Varfolomeeva Victoria
'''
import math
import turtle
def triangle(x,y,a,b,c,angle,color,fill, border,border_color):
    '''
    Function for drawing triangle.
    :param x: coordinate x
    :param y: coordinate y
    :param a: leg 1
    :param b: leg 2
    :param angle: angle of rotation
    :param color: color of triangle
    :param fill: color of the fill
    :param border: breadth of limit
    :param border-color: color of the border
    :return: None
    '''
    pass
    goto(x,y)
    color(color, fill)
    pensize(border)
    begin_fill()
    pd()
    fd(a)


def rectangle(x,y,a,b,color,border,border_color):
    '''
    Function for drawing rectangle.
    :param x: coordinate x
    :param y: coordinate y
    :param a: width
    :param b: length
    :param color: color of rectangle
    :param border: breadth of limit
    :param border_color: color of the border
    :return: none
    '''
    pass
def ellipse(a, b, color, fill):
    '''
    Function for drawing ellipse
    :param a: radius of the bigger circle of the ellipse
    :param b: radius of the smaller circle of the ellipse
    :param color: color of border
    :param fill: color of filling
    :return: none
    '''
    dx = turtle.xcor()
    dy = turtle.ycor()
    turtle.color(color, fill)
    turtle.begin_fill()
    for deg in range(361):
        rad = math.radians(deg)
        x = a * math.sin(rad) + dx
        y = -b * math.cos(rad) + b + dy
        turtle.goto(x, y)
    turtle.end_fill()
def main():
    '''
    Main function.
    :return: None
    '''

if __name__ == '__main':
    main()