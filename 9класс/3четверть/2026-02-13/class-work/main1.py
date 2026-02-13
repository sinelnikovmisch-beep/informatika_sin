import turtle as t


t.speed(0)
f= 40
n = 10
def parse(str):
    for symbol in str:
        if symbol == 'F':
            t.forward(f)
        if symbol == 'L':
            t.left(60)
        if symbol == 'R':
            t.right(60)

def parsePlus(str, n):
    if n == 0:
        parse(str)
        return
    for symbol in str:
        if symbol == 'F':
            parsePlus(str, n-1)
        if symbol == 'L':
            t.left(60)
        if symbol == 'R':
            t.right(60)

def snow_flake(str, n):
    for i in range(3):
        parsePlus(str, n)
        t.right(120)

def dragon(str, n):
    if n==0:
        parse(str)
        return
    for symbol in str:
        if symbol == 'X':
            dragon("XLYFL", n-1)
        if symbol == 'Y':
            dragon("RFXRY", n-1)
        if symbol == 'F':
            t.forward(f)
        if symbol == 'L':
            t.left(60)
        if symbol == 'R':
            t.right(60)



f = f/n
# snow_flake("FLFRRFLF", n)
dragon("FX", n)
t.done()