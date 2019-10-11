import math as m

step = 0.5
state = 0 # 1 - нечет 2 - чет 0 - общ
eps = 0.000005
def f(x):
	return x**4

x=-5


print("x^4:")
while x<=5:
	if f(-x)-eps<=f(x)<=f(-x)+eps:
		state = 2
	elif f(-x)-eps<=-f(x)<=f(-x)+eps:
		state = 1
	else:
		state = 0
	x+=step


	
print(state)

x=-5

print("tg")
while x<=5:
	if m.tan(-x)-eps<=m.tan(x)<=m.tan(-x)+eps:
		state = 2
	elif m.tan(-x)-eps<=-m.tan(x)<=m.tan(-x)+eps:
		state = 1
	else:
		state = 0
	x+=step


	
print(state)

x=-5

print("exp")
while x<=5:
	if m.exp(-x)-eps<=m.exp(x)<=m.exp(-x)+eps:
		state = 2
	elif m.exp(-x)-eps<=-m.exp(x)<=m.exp(-x)+eps:
		state = 1
	else:
		state = 0
	x+=step


	
print(state)