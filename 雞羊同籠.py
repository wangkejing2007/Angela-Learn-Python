from sympy import *
#已知雞加羊的數目為20隻，雞加羊共有50隻腳，求雞的數量
print()

#一元一次
x = Symbol('x') #雞的數目
print(solve(2*x + 4*(20-x)-50,x))
print()

#二元一次 
y,z = symbols('y z')
print(solve([y+z-10, 2*y+z-16], [y,z]))
print()