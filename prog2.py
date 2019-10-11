import math as m

print("sin^2")
T = float(input("Введите период"))
state = 0 # 1 - период 0 - непериод
step = T/30
eps = T/1000



def f(x):
	return m.sin(x)**2

x = 0
while x<=5*T:
	if f(x+T)-eps<=f(x)<=f(x+T)+eps:
		state = 1
	else:
		state = 0
	x+=step
print(state)

print("tg")
T = float(input("Введите период"))
x = 0
while x<=5*T:
	if m.tan(x+T)-eps<=m.tan(x)<=m.tan(x+T)+eps:
		state = 1
	else:
		state = 0
	x+=step
print(state)

print("1/2*sin")
T = float(input("Введите период"))
x = 0
while x<=5*T:
	if m.sin(x+T)/2.0-eps<=m.sin(x)/2.0<=m.sin(x+T)/2.0+eps:
		state = 1
	else:
		state = 0
	x+=step
print(state)
