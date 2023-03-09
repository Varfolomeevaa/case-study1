'''
Title 
Group:
Sineokaya Anastasia
Varfolomeeva Victoria
'''
import math
import turtle
def triangle(x,y,a,b,fill,border,border_color):
    '''
    Function for drawing triangle.
    :param x: coordinate x
    :param y: coordinate y
    :param a: leg 1
    :param b: leg 2
    :param fill: color of the fill
    :param border: breadth of limit
    :param border-color: color of the border
    :return: None
    '''
    turtle.pu()
    turtle.goto(x,y)
    turtle.color(border_color, fill)
    turtle.pensize(border)
    turtle.begin_fill()
    turtle.pd()
    turtle.lt(90)
    turtle.fd(a)
    turtle.rt(90)
    turtle.fd(b)
    turtle.goto(x,y)
    turtle.end_fill()
    turtle.pu()
    pass
triangle(50,50,215,124,'red', 5,'blue' )

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
def ellipse(a, b, color, fill,x0,y0):
    '''
    Function for drawing ellipse
    :param a: radius of the bigger circle of the ellipse
    :param b: radius of the smaller circle of the ellipse
    :param color: color of border
    :param fill: color of filling
    :param x0: coordinate x0
    :param y0: coordinate y0
    :return: None
    '''
    turtle.pu()
    turtle.goto(x0,y0)
    dx = turtle.xcor()
    dy = turtle.ycor()
    turtle.pd()
    turtle.color(color, fill)
    turtle.begin_fill()
    for deg in range(361):
        rad = math.radians(deg)
        x = a * math.sin(rad) + dx
        y = -b * math.cos(rad) + b + dy
        turtle.goto(x, y)
    turtle.end_fill()
    pass
def main():
    '''
    Main function.
    :return: None
    '''

if __name__ == '__main':
    main()