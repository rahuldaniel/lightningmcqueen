import sys
#3import matplotlib.pyplot as plt
n=int(input("any whole number"))
#x = []
#y = []
#c=0
while True:
	if n==1:
#		plt.scatter(x, y)
#		plt.show()
		sys.exit()		
	elif (n%2)==0:
		n = n/2
		print(n)
	elif (n%2) ==1:
		n = 3*n+1
		print(n)
#	x.append(n)
#	c=c+1
#	y.append(c)
