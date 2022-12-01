f=open("input.txt","r")
ans=0
cur=0
for line in f:
	if len(line)==1:
		ans=max(ans,cur)
		cur=0
	else:
		cur+=int(line)
print(ans)