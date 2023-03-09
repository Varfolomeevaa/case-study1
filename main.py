'''
Title 
Group:
Sineokya Anastasia
Varfolomeeva Victoria
'''
import turtle
import math
def triangle(x,y,a,b,angle,color, border,border_color):
    '''
    Function for drawing triangle.
    :param x: coordinate x
    :param y: coordinate y
    :param a: leg 1
    :param b: leg 2
    :param angle: angle of rotation
    :param color: color of triangle
    :param border: breadth of limit
    :param border_color: color of the border
    :return: None
    '''
    pass

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
def ellipse(a, b, color='black', fill=''):
    '''
    Function for drawing ellipse
    :param a:
    :param b:
    :param color:
    :param fill:
    :return:
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