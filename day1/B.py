f=open("input.txt","r")
cal=[]
cur=0
for line in f:
	if len(line)==1:
		cal.append(cur)
		cur=0
	else:
		cur+=int(line)
cal.sort()
cal.reverse()
print(cal[0]+cal[1]+cal[2])