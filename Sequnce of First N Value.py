'''This will generate a sequence of first N Values'''

#declaring the generatro fucntion
def mygen(N):
	i=1
	while i<=N:
		yield i
		i=i+1
#calling function with required Value
gen=mygen(10)

#Print the values
for value in gen:
	print(value)
