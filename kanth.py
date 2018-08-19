def odd(a1,b):
	if((a1%2)==0):
		if(abs(b-a1)==1 or abs(b-a1)==0):
			print("no odd numbers")
		a1=a1+1
		while(a1!=b and a1!=(b+1)):
			print(a1)
			a1=a1+2
	else:
		if(abs(b-a1)==2 or abs(b-a1)==1):
			print("no odd numbers")
		a1=a1+2
		while(a1!=b and a1!=(b+1)):
			print(a1)
			a1=a1+2
a1,b=[int(x) for x in raw_input().split(",")]
if(a1<b):
	odd(a1,b)
			
elif(a1>b):
	temp=a
	a1=b
	b=temp
	odd(a1,b)
else:
	odd(a1,b)
