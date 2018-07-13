'''
Tests for the StartPy library
This file should print only True, objects, or caught exception errors
'''
from StartPy import *

turret = Rectangle(50, 25, GREEN, 25, 0)
body = Oval(100, 30, BLACK, 0, 20)
barrel = Rectangle(30, 5, ORANGE, 75, 5)
tank = turret + body + barrel
co = Square(50, RED) + Square(50, BLUE_VIOLET, 25, 25)

add(tank, -100, -100)
print(not inWorld(body))
print(inWorld(tank))
remove(tank)
add(tank, 100, 100)
print(not inWorld(barrel))
print(inWorld(tank))
add(co)
print(inWorld(co))
remove(co)
print(not inWorld(co))
add(co)
removeAll()
print(not inWorld(tank))
print(not inWorld(co))
co.move(1, 1)
co.move(-1, -1)
add(co, 300, 300)
c = Circle(50, GRAY)
add(Circle(50, GRAY))
add(c, 100, 100)
print(objectAtXY(300, 300))
print(objectAtXY(360, 360))
remove(objectAtXY(100, 100)) # finds GO at xy
remove(objectAtXY(300, 300)) # works if xy is initial object add location
add(Circle(50, PINK), 200, 200)
print(objectAtXY(200, 200))
remove(objectAtXY(200, 200))
# remove(objectAtXY(200, 200))
print(objectAtXY(200, 200) == None)
c = Circle(50, PINK)
add(c, 200, 200)
c.move(100, 100)
print(objectAtXY(200, 200) == None)
print(objectAtXY(300, 300))
remove(objectAtXY(300, 300))
add(c, 200, 200)
remove(c)
add(c, 300, 300)
print(objectAtXY(200, 200) == None)
print(objectAtXY(300, 300))
remove(objectAtXY(300, 300))
print(objectAtXY(300, 300) == None)
removeAll()

# objectAts
o = Circle(20, PINK)
co = Square(20, BLUE_VIOLET) + Oval(25, 10, MAGENTA, 10)
add(o, 100, 0)
remove(o)
add(o, 50, 0)
print(objectAtXY(50, 0))
print(objectAtXY(100, 0) == None)
add(co)
remove(co)
add(co, 0, 50)
print(objectAtXY(0, 0) == None)
print(objectAtXY(0, 50))
co.move(50, 0)
print(objectAtXY(50, 50))
print(objectAtLocation((50, 50)))
print(objectAtLocation((50, 0)))

# collides
r = Rectangle(50, 10, BLACK)
add(r)
print(not collides(r, o)) # o is 20 pink circle
r.move(1, 0)
print(collides(r, o))
o2 = Circle(20, RED)
add(o2, 65, 15)
print(collides(o, o2))
co2 = Circle(25, BLUE) + Circle(40, BEIGE, 10, 0)
add(co2, 50, 80)
print(objectAtXY(50, 50)) # purple/pink co
print(objectAtXY(50, 80))
print(not collides(co, co2))
co2.move(0, -20)
print(collides(co, co2))
print(collides(co2, co))
co2.move(20, 10)
print(not collides(co, co2))
co2.move(0, -1)
print(collides(co, co2))
r = Rectangle(100, 200, RED) + Rectangle(100, 200, BLUE_VIOLET, 100, 0)
z = Circle(150, BLACK)
add(r)
add(z)
print(collides(r, z))
removeAll()

# object stacking
o1 = Rectangle(100, 200, RED) + Rectangle(100, 200, BLUE_VIOLET, 100, 0)
o2 = Circle(150, BLACK) + Circle(150, BLACK, 70, 0)
o3 = Square(100, PINK) + Circle(200, PALE_TURQUOISE, 100)
add(o1)
add(o2, 0, 35)
add(o3)
sendForward(o1)
sendBackward(o1)
sendBackward(o2)
sendBackward(o3)
sendForward(o2)
sendForward(o3)
sendToFront(o2)
sendToBack(o1)

# object setters
o1.setLocation(200, 200)
add(Square(200, BLACK))
remove(objectAtXY(199, 199))
print(objectAtXY(199, 199))
o1.setVisible(False)
o1.setVisible(True)
o1.move(10, 10)

# object getters
print(o1.getX() == 210)
print(o1.getY() == 210)
print(o1.getLocation() == (210, 210))
o4 = Square(20, BLACK) + Square(20, BLACK, 300, 300)
add(o4)
print(o4.getLocation() == (0, 0))
print(o4.getX() == 0)
print(o4.getY() == 0)
print(o4.getColor() == (255, 255, 255))
print(o1.getColor() == (255, 255, 255))
print(o1.getVisible())
o1.setVisible(False)
print(not o1.getVisible())
o1.setVisible(True)
print(o1.getWidth() == 200)
print(o1.getHeight() == 200)
print(inWorld(o1))
o1.move(200, 200)
print(inWorld(o1))
o1.move(100, 100)
print(inWorld(o1))

# error catching
c = Circle(10, RED)
add(c)
print()
try:
    add(Circle(RED, 10))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Circle(10, 10))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Circle(10, RED, BLUE, 10))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Circle(10, RED, 10, BLUE))
    print('no exception')
except ValueError as e:
    print(e)
try:
    c.setDiameter(RED)
    print('no exception')
except ValueError as e:
    print(e)
try:
    c.setSize(RED)
    print('no exception')
except ValueError as e:
    print(e)


r = Rectangle(10, 10, BLUE)
add(r)
print()
try:
    add(Rectangle(BLACK, 10, RED, 10, 10))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Rectangle(10, BLACK, RED, 10, 10))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Rectangle(10, 10, 5, 10, 10))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Rectangle(10, 10, RED, BLACK, 10))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Rectangle(10, 10, RED, 10, BLACK))
    print('no exception')
except ValueError as e:
    print(e)
try:
    r.setSize(BLACK, 10)
    print('no exception')
except ValueError as e:
    print(e)
try:
    r.setSize(10, BLACK)
    print('no exception')
except ValueError as e:
    print(e)
try:
    r.setHeight(BLACK)
    print('no exception')
except ValueError as e:
    print(e)
try:
    r.setWidth(BLACK)
    print('no exception')
except ValueError as e:
    print(e)

o = Oval(10, 20, BLUE)
add(o)
print()
try:
    add(Oval(BLACK, 20, BLUE, 10, 10))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Oval(10, BLACK, BLUE, 10, 10))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Oval(10, 20, 0, 10, 10))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Oval(10, 20, BLUE, BLACK, 10))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Oval(10, 20, BLUE, 10, BLACK))
    print('no exception')
except ValueError as e:
    print(e)
try:
    o.setSize(BLACK, 10)
    print('no exception')
except ValueError as e:
    print(e)
try:
    o.setSize(10, BLACK)
    print('no exception')
except ValueError as e:
    print(e)
try:
    o.setHeight(BLACK)
    print('no exception')
except ValueError as e:
    print(e)
try:
    o.setWidth(BLACK)
    print('no exception')
except ValueError as e:
    print(e)


s = Square(10, BLUE)
add(s)
print()
try:
    add(Square(BLACK, BLUE, 10, 10))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Square(10, 10, 10, 10))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Square(10, BLUE, BLACK, 10))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Square(10, BLUE, 10, BLACK))
    print('no exception')
except ValueError as e:
    print(e)
try:
    o.setSize(BLACK, 10)
    print('no exception')
except ValueError as e:
    print(e)
try:
    o.setSize(10, BLACK)
    print('no exception')
except ValueError as e:
    print(e)
try:
    o.setWidth(BLACK)
    print('no exception')
except ValueError as e:
    print(e)

# labels
l = Label(12, RED, 'HELLO', 100, 100)
add(l)
print()
try:
    add(Label(BLACK, RED, 'HELLO', 100, 100))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Label(12, 10, 'HELLO', 100, 100))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Label(12, RED, 1, 100, 100))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Label(12, RED, 'HELLO', BLUE, 100))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Label(12, RED, 'HELLO', 100, BLACK))
    print('no exception')
except ValueError as e:
    print(e)
try:
    l.setFontSize(BLACK)
    print('no exception')
except ValueError as e:
    print(e)
try:
    l.setText(BLACK)
    print('no exception')
except ValueError as e:
    print(e)

# more error throwing
circ = Circle(10, BLACK)
add(circ)
com = Circle(50, BLUE) + Oval(100, 100, BLACK)

# tested statements that throw exceptions...
try:
    add(Square(200, makeColorRGB(-200, 100, 255)))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Square(200, makeColorRGB('fish', 100, 255)))
    print('no exception')
except ValueError as e:
    print(e)
print()
try:
    add(Square(200, makeColorHex('j6A77B')))
    print('no exception')
except ValueError as e:
    print(e)
try:
    add(Square(200, makeColorHex('f6A')))
    print('no exception')
except ValueError as e:
    print(e)
try:
    inWorld(BLUE)
    print('no exception')
except Exception as e:
    print(e)
try:
    add('his')
    print('no exception')
except Exception as e:
    print(e)
try:
    remove(BLACK)
    print('no exception')
except Exception as e:
    print(e)
try:
    setCaption(BLUE)
    print('no exception')
except Exception as e:
    print(e)
try:
    setWidth(BLUE)
    print('no exception')
except Exception as e:
    print(e)
try:
    setHeight('him')
    print('no exception')
except Exception as e:
    print(e)
try:
    setSize(100, BLUE)
    print('no exception')
except Exception as e:
    print(e)
try:
    setColor('yellow')
    print('no exception')
except Exception as e:
    print(e)
try:
    pause(BLUE)
    print('no exception')
except Exception as e:
    print(e)
try:
    objectAtXY(BLUE, 100)
    print('no exception')
except Exception as e:
    print(e)
try:
    objectAtLocation(BLUE)
    print('no exception')
except Exception as e:
    print(e)
try:
    sendForward('hi')
    print('no exception')
except Exception as e:
    print(e)
try:
    sendBackward(BLUE)
    print('no exception')
except Exception as e:
    print(e)
try:
    sendToBack(1)
    print('no exception')
except Exception as e:
    print(e)
try:
    sendToFront(BLACK)
    print('no exception')
except Exception as e:
    print(e)
try:
    collides(BLUE, circle_ex)
    print('no exception')
except Exception as e:
    print(e)
try:
    circ.move(100, 'ch')
    print('no exception')
except Exception as e:
    print(e)
try:
    com.move(100, BLACK)
    print('no exception')
except Exception as e:
    print(e)
try:
    circ.setLocation(BLUE, BLACK)
    print('no exception')
except Exception as e:
    print(e)
try:
    com.setLocation(100, BLACK)
    print('no exception')
except Exception as e:
    print(e)
try:
    circ.setColor(10)
    print('no exception')
except Exception as e:
    print(e)
try:
    circ.setVisible(100)
    print('no exception')
except Exception as e:
    print(e)
try:
    com.setVisible(BLACK)
    print('no exception')
except Exception as e:
    print(e)
try:
    com.setObjectColor(1, 1)
    print('no exception')
except Exception as e:
    print(e)

removeAll()

l = Label(100, RED, 'Test Label', 20, 20)
l.setColor(BLACK)
print(l.getColor() == (0, 0, 0))
add(l)

b = Button('Button', 50, PINK, BLUE, 30, 100)
add(b)
b.setWidth(100)
print(b.getWidth() == 100)
b.setHeight(50)
print(b.getHeight() == 50)

l.setHeight(15)
print(l.getHeight() == 15)
l.setWidth(300)
print(l.getWidth() == 300)

removeAll()

gcomp = Button('One', 30, RED, BLACK) + Button('Two', 30, TEAL, BLACK, 54)
add(gcomp, 100, 100)
print(gcomp.getLocation() == (100, 100))
gcomp.move(100, -100)
print(gcomp.getLocation() == (200, 0))
gcomp.setLocation(0, 0)
print(gcomp.getLocation() == (0, 0))
gcomp.move(100, 200)
print(gcomp.getLocation() == (100, 200))
gcomp.setVisible(False)
print(not gcomp.getVisible())
gcomp.setVisible(True)
print(gcomp.getVisible())

brect = Button('One', 30, RED, BLACK) + Rectangle(50, 25, BLUE, 54, 0)
add(brect, 0, 100)
print(brect.getLocation() == (0, 100))

brect.move(0, 200)
print(brect.getLocation() == (0, 300))

brect.setLocation(100, 0)
print(brect.getLocation() == (100, 0))

b.setFontSize(100)
print(100 == b.getFontSize())
b.setWidth(300)
print(300 == b.getWidth())
brect.setObjectColor(1, BLACK)

removeAll()

rec = Rectangle(100, 100, GREEN)
add(rec, 400, 0)

start()

ci = Image('ball.png') + Image('ball.png', 50, 0) + Rectangle(40, 20, RED, 30, 15) + Circle(20, BLUE, 20) +\
     Square(20, GRAY)
ci2 = Image('ball.png') + Image('ball.png', 50, 0) + Rectangle(40, 20, RED, 30, 15) + Circle(20, BLUE, 20) +\
     Square(20, GRAY) + Button('One', 30, RED, BLACK, 0, 50) + Button('Two', 30, TEAL, BLACK, 50, 50) + Label(18, BLUE, 'LABEL', 30, 20)
add(ci, 25, 0)
add(ci2)
ci2.setWidth(300)
ci2.setHeight(50)

ci.setLocation(0, 0)

c = Circle(10, BLACK)
add(c)
c.setScale(10)
print(c.getDiameter() == 100)
c.setWidth(200)
c.setHeight(200)
print(c.getHeight() == 200 and c.getWidth() == 200 and c.getDiameter() == 200)
c.setSize(20)
print(c.getDiameter() == 20)
s = Square(10, BLACK)
add(s)
s.setScale(20)
print(s.getWidth() == 200 and s.getHeight() == 200)
o = Oval(300, 100, BLANCHED_ALMOND)
add(o)
o.setScale(.5)
print(o.getHeight() == 50 and o.getWidth() == 150)
o.setHeight(150)
print(o.getHeight() == 150)
im = Image('img.jpg')
add(im)
print(collides(im, o))
width = im.getWidth()
im.setScale(3)
print(im.getWidth() == 3*width)

im.setBackground()
print(getBackground() == im)
remove(getBackground())
s.move(200, 200)
o.move(200, 200)
ci.setLocation(0, 400)
ci.setWidth(480)
print(ci.getWidth() == 480)
ci.setWidth(200)
ci.setHeight(170)
ci.move(0, -200)
print(not collides(ci, im))
o.setBackground()

try:
    setBackground('yellow')
    print('no exception')
except Exception as e:
    print(e)
b4 = Button('One', 30, RED, BLACK, 0, 50)
add(b4)
try:
    b4.setBackground()
    print('no exception')
except Exception as e:
    print(e)
remove(b4)

remove(ci2)
add(ci2)
ci2.setBackground()
remove(o)
remove(s)

stop()
