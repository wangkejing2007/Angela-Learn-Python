from sympy import *
print()

#一元一次
#已知雞加兔的數目為20隻，雞加兔共有50隻腳，求雞的數量？
#一元一次(symbol)
x = Symbol('x') #x表示雞的數目
print(solve(2*x + 4*(20-x)-50,x))
print()

#二元一次(symbols)比較 
y,z = symbols('y z') #y表示雞的數目，z表示兔的數目
print(solve([y+z-20, 2*y+4*z-50], [y,z]))
print()