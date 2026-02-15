import turtle as t

def elochka(n, a, x, d):
    t.left(90)
    t.forward(a*n)
    for i in range(n):
        t.left(100)
        t.forward(x+d*i)
        t.teleport(0, a*(n-i))
        t.right(100)
        t.right(100)
        t.forward(x+d*i)
        t.teleport(0, a*(n-i-1))
        t.left(100)

elochka(3, 40, 20, 10)

t.done()
