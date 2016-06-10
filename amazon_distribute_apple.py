n=4
num_of_apple = [1,3,9,7]
total = 0
for i in range(n):
	total += num_of_apple[i]
total = total/n
import pdb;pdb.set_trace()
neg=[0]*n
for i in range(n):
	neg[i]=num_of_apple[i]-total
p=0
cum=[0]*n
for i in range(n):
	cum[i]=p
	p+=neg[i]
cum.sort()
med=0
if n%2==0:
	med=(cum[(n-1)/2]+cum[n/2])/2
else:
	med=cum[n/2]
ans=0
for i in range(n):
	ans+=abs(cum[i]-med)
print ans