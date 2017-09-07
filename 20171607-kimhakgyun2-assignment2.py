a=1
qs=1
while(qs!= -1):
	qs = int(input('Enter the number : '))
	for i in range(qs):
		a = a * (i+1)
	if(qs != -1):
		print("%d! = %d" %(qs, a))
	a = 1
		
