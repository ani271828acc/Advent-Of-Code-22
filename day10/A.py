f=open("input.txt","r")
req=[20+40*i for i in range(6)]
[cyc,val,ans]=[1,1,0]
for line in f:
	if line[0]=='n':
		if cyc in req:
			ans+=val*cyc
		cyc+=1
	else:
		if cyc in req:
			ans+=val*cyc
		elif cyc+1 in req:
			ans+=val*(cyc+1)
		cyc+=2
		val+=int(line[0:len(line)-1].split()[-1])
if cyc in req:
	ans+=val*cyc
print(ans)