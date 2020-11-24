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
    k_1 = f(t,y)
    k_2 = f(t + 0.5*h, y + 0.5*h*k_1)
    k_3 = f(t + 0.5*h, y + 0.5*h*k_2)
    k_4 = f(t + h, y + h*k_3)
    y = y + (k_1 + 2*k_2 + 2*k_3 + k_4) * (h/6)
    t += h
    print('{:.3f}'.format(t) + ': ' + str(y))
