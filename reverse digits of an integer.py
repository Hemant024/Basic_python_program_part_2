# Problem Description:	You are given a positive number N and 
# 						you need to generate the reverse of a given number N.

# Note: 		If a number has trailing zeros, then its reverse will not include them. 
# For e.g.,   the reverse of 10400 will be 401 instead of 00401.


n= int(input())
temp = n
revNum = 0
while temp > 0 :
	lastDigit = temp % 10
	revNum = revNum * 10 + lastDigit
	temp = temp // 10
print(revNum)