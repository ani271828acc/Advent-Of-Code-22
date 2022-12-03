f=open("input.txt","r")
res=0
pr={}
for i in range(26):
	pr[chr(ord('a')+i)]=i+1
	pr[chr(ord('A')+i)]=27+i

for line in f:
	ct={}
	for c in line[0:len(line)//2]:
		ct[c]=1
	for c in line[len(line)//2:len(line)-1]:
		if c in ct:
			res+=pr[c]
			break
print(res)
