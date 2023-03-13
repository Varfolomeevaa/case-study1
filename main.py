'''
Title 
Group:
Sineokaya Anastasia
Varfolomeeva Victoria
'''
import math
import turtle
def rectangle(x,y,a,b,fill,border,border_color):
    '''
    Function for drawing rectangle.
    :param x: coordinate x
    :param y: coordinate y
    :param a: width
    :param b: length
    :param fill: color of rectangle
    :param border: breadth of limit
    :param border_color: color of the border
    :return: none
    '''
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

def triangle(x,y,a,b,ang1,ang2,fill):
    '''
    Function for drawing triangle.
    :param x: coordinate x
    :param y: coordinate y
    :param a: leg 1
    :param b: leg 2
    :param ang1: 1st angle of rotation
    :param ang2: 2nd angle of rotation
    :param fill: color of the fill
    :return: None
    '''
    turtle.speed(5)
    turtle.pu()
    turtle.goto(x,y)
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

def ellipse(a, b, color, fill,x0,y0,border):
    '''
    Function for drawing ellipse
    :param a: radius of the bigger circle of the ellipse
    :param b: radius of the smaller circle of the ellipse
    :param color: color of border
    :param fill: color of filling
    :param x0: coordinate x0
    :param y0: coordinate y0
    :param border: breadth of limit
    :return: None
    '''
    turtle.pu()
    turtle.goto(x0,y0)
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
def semicircle(r,x0,y0,color,fill,border):
    '''
    Function for drawing semicircle
    :param r: radius of semicircle
    :param x0: coordinate x0
    :param y0: coordinate y0
    :param color: color of border
    :param fill: color of filling
    :param border: breadth of limit
    :return: None
    '''
    turtle.pu()
    turtle.goto(x0, y0)
    turtle.pd()
    turtle.color(color,fill)
    turtle.pensize(border)
    turtle.begin_fill()
    turtle.circle(r,180)
    turtle.rt(90)
    turtle.bk(r*2)
    turtle.end_fill()
    pass
def sector(r,x0,y0,color,fill,border,ang):
    '''
    Function for drawing semicircle
    :param r: radius of sector
    :param x0: coordinate x0
    :param y0: coordinate y0
    :param color: color of border
    :param fill: color of filling
    :param border: breadth of limit
    :return: None
    '''
    turtle.pu()
    turtle.goto(x0, y0)
    turtle.lt(ang)
    turtle.pd()
    turtle.color(color,fill)
    turtle.pensize(border)
    turtle.begin_fill()
    turtle.circle(r,90)
    turtle.rt(90)
    turtle.bk(r)
    turtle.rt(90)
    turtle.fd(r)
    turtle.rt(ang-90)
    turtle.end_fill()
    pass

triangle(-300,300,150,150,-90,-90,'white')
triangle(-150,150,150,150,90,-90,'lightsteelblue')
triangle(-150,150,150,150,90,90,'darkslateblue')
triangle(0,300,150,150,-90,90,'plum')
triangle(0,300,150,150,-90,-90,'lightsteelblue')
triangle(150,150,150,150,90,-90,'darkslateblue')
rectangle(150,150,150,150,'white',0,'')
sector(150,300,150,'','orangered',0,90)
triangle(300,0,150,150,90,-90,'darkslateblue')
triangle(150,150,150,150,-90,-90,'lightsteelblue')
sector(150,150,0,'','darkslateblue',0,90)
sector(150,0,150,'','darkslateblue',0,180)
rectangle(-300,0,150,150,'lightsteelblue',0,'')
#rectangle(-300,-300,600,600,'',1, 'black')
turtle.done()

def main():
    '''
    Main function.
    :return: None
    '''

if __name__ == '__main':
    main()