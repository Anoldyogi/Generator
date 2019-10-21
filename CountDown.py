'''this is just countdown from N '''

import time

#fucntion to generate the sequence
def countdown(N):
	while N>=0:
		yield N
		N=N-1

#calling function and assigning sequence
gen=countdown(10)

#printing vlaues from sequence
for value in gen:
	print(value)
	time.sleep(1)
