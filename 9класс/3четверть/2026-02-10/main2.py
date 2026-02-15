import turtle as t

def f(x):
    return x*x + 2*x -2

def drawF(n):
    t.teleport(-n, 0)
    t.forward(2*n)
    t.left(90)
    t.teleport(0, -n)
    t.forward(2*n)
    t.teleport(-n, f(n))
    for i in range(-n, n+1):
        t.goto(i, f(i))

drawF(20)

t.done()