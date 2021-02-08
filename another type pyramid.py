# Print the following pattern for the given N number of rows.
# Pattern for N = 5
#  A
#  BB
#  C*C
#  D**D
#  E***E


n= 6
y=0
if n > 0:
	print("A")
if n > 1:
	print("BB")
if n > 2:
	for i in range(1,n-1):
		print(chr(66+i) + "*"*i + chr(66+i))
		y+=1