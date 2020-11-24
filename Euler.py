import math

valid = False
while (not valid):
    try:
        func = str(input('Function: '))
        f = lambda t, y: eval(func)
        f(1, 1)
    except:
        print("\nInvalid function!\n")
    else:
        valid = True

t = float(input('t_0: '))
y = float(input('y_0: '))
h = float(input('h: '))
n = int(input('n: '))
print()

for i in range(n):
    y = y + f(t,y)*h
    t += h
    print('{:.1f}'.format(t) + ': ' + str(y))