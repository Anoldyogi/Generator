'''Program to generate first N fibonacci Series'''

def fibonacci():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b

gen=fibonacci()
count=1
N=int(input("Enter how many fibonacci numbers you want"))
while count<=N:
	print(next(gen))
	count=count+1
