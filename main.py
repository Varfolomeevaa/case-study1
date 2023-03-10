"""
Title 
Group:
Sineokaya Anastasia 60
Varfolomeeva Victoria 70
"""
import math
import turtle


def rectangle(x, y, a, b, fill, border, border_color):
    """
    Function for drawing rectangle.
    :param x: coordinate x
    :param y: coordinate y
    :param a: length
    :param b: width
    :param fill: color of rectangle
    :param border: breadth of limit
    :param border_color: color of the border
    :return: none
    """
    turtle.pu()
    turtle.goto(x, y)
    turtle.color(border_color, fill)
    turtle.pensize(border)
    turtle.begin_fill()
    turtle.pd()
    turtle.lt(90)
    turtle.fd(a)
    turtle.rt(90)
    turtle.fd(b)
    turtle.rt(90)
    turtle.fd(a)
    turtle.rt(90)
    turtle.fd(b)
    turtle.rt(180)
    turtle.end_fill()
    turtle.pu()
    pass


def triangle(x, y, a, b, ang1, ang2, fill):
    """
    Function for drawing triangle.
    :param x: coordinate x
    :param y: coordinate y
    :param a: leg 1
    :param b: leg 2
    :param ang1: 1st angle of rotation
    :param ang2: 2nd angle of rotation
    :param fill: color of the fill
    :return: None
    """
    turtle.pu()
    turtle.goto(x, y)
    turtle.color(fill)
    turtle.pensize(1)
    turtle.begin_fill()
    turtle.pd()
    turtle.lt(ang1)
    turtle.fd(a)
    turtle.rt(ang2)
    turtle.fd(b)
    turtle.lt(180-ang1-ang2)
    turtle.end_fill()
    turtle.pu()
    pass


def ellipse(a, b, color, fill, x0, y0, border):
    """
    Function for drawing ellipse.
    :param a: radius of the bigger circle of the ellipse
    :param b: radius of the smaller circle of the ellipse
    :param color: color of border
    :param fill: color of filling
    :param x0: coordinate x0
    :param y0: coordinate y0
    :param border: breadth of limit
    :return: None
    """
    turtle.pu()
    turtle.goto(x0, y0)
    dx = turtle.xcor()
    dy = turtle.ycor()
    turtle.pd()
    turtle.color(color, fill)
    turtle.pensize(border)
    turtle.begin_fill()
    for deg in range(361):
        rad = math.radians(deg)
        x = a * math.sin(rad) + dx
        y = -b * math.cos(rad) + b + dy
        turtle.goto(x, y)
    turtle.end_fill()
    pass


def sector(r, x0, y0, color, fill, border, ang):
    """
    Function for drawing sector.
    :param r: radius of sector
    :param x0: coordinate x0
    :param y0: coordinate y0
    :param color: color of border
    :param fill: color of filling
    :param border: breadth of limit
    :param ang: angle of rotation
    :return: None
    """
    turtle.pu()
    turtle.goto(x0, y0)
    turtle.lt(ang)
    turtle.pd()
    turtle.color(color, fill)
    turtle.pensize(border)
    turtle.begin_fill()
    turtle.circle(r, 90)
    turtle.rt(90)
    turtle.bk(r)
    turtle.rt(90)
    turtle.fd(r)
    turtle.rt(ang-90)
    turtle.end_fill()
    pass


def part_1():
    """
    Function for part 1.
    :return: None
    """
    triangle(-300, 300, 150, 150, -90, -90, 'white')
    triangle(-150, 150, 150, 150, 90, -90, 'lightsteelblue')
    triangle(-150, 150, 150, 150, 90, 90, 'darkslateblue')
    triangle(0, 300, 150, 150, -90, 90, 'plum')
    triangle(0, 300, 150, 150, -90, -90, 'lightsteelblue')
    triangle(150, 150, 150, 150, 90, -90, 'darkslateblue')
    rectangle(150, 150, 150, 150, 'white', 0, '')
    sector(150, 300, 150, '', 'orangered', 0, 90)
    triangle(300, 0, 150, 150, 90, -90, 'darkslateblue')
    triangle(150, 150, 150, 150, -90, -90, 'lightsteelblue')
    rectangle(-150, 0, 150, 300, 'white', 0, '')
    sector(150, 150, 0, '', 'darkslateblue', 0, 90)
    sector(150, 0, 150, '', 'darkslateblue', 0, 180)
    rectangle(-300, 0, 150, 150, 'lightsteelblue', 0, '')
    sector(150, -300, 0, '', 'orangered', 0, 0)
    pass


def part_2():
    """
    Function for part2.
    :return: None
    """
    triangle(-300, -150, 150, 150, 90, 90, 'white')
    triangle(-300, -150, 150, 150, 0, 270, 'plum')
    triangle(0, -150, 150, 150, 180, 90, 'lightsteelblue')
    triangle(0, -150, 150, 150, 90, 270, 'white')
    triangle(-150, -300, 150, 150, 180, 90, 'orangered')
    triangle(-300, -150, 150, 150, 0, 90, 'darkslateblue')
    triangle(0, -150, 150, 150, 180, 270, 'white')
    triangle(-150, -300, 150, 150, 0, 270, 'plum')

    rectangle(0, -150, 150, 150, 'gold', 0, '')
    sector(150, 0, -150, '', 'plum', 0, 0)
    rectangle(150, -150, 150, 150, 'orangered', 0, '')
    ellipse(75, 75, '', 'white', 225, -150, 0)
    rectangle(150, -150, 150, 150, '', 0, 'orangered')
    rectangle(0, -300, 150, 75, 'lightsteelblue', 0, '')
    rectangle(75, -300, 150, 75, 'white', 0, '')
    rectangle(150, -300, 150, 150, 'lightsteelblue', 0, '')
    sector(150, 300, -300, '', 'plum', 0, 90)
    rectangle(-300, -300, 600, 600, '', 10, 'black')
    pass


def main():
    """
    Main function.
    :return: None
    """
    turtle.speed(10)
    turtle.ht()
    turtle.bgcolor('lavender')
    part_1()
    part_2()
    turtle.done()
    pass


if __name__ == '__main__':
    main()
