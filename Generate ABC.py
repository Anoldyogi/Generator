'''This is just for syntax'''

def mygen():
	yield 'A'
	yield 'B'
	yield 'C'

#creating object
gen=mygen()

#printing each value
for value in gen:
	print(value)
