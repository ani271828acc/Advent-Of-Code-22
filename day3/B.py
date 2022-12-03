f=open("input.txt","r")
pr={}
for i in range(26):
	pr[chr(ord('a')+i)]=i+1
	pr[chr(ord('A')+i)]=27+i

lines=[line for line in f]
res=0
for i in range(0,len(lines),3):
	for c in lines[i]:
		if c in lines[i+1] and c in lines[i+2]:
			res+=pr[c]
			break
print(res)