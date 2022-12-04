f=open("input.txt","r")
res=0
pres=0
for line in f:
	r=sorted([[int(i) for i in s.split('-')] for s in line.split(',')])
	res+=int(r[0][1]>=r[1][0])
print(res)