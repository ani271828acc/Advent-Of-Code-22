f=open("input.txt","r")
line=f.read()
count=4
for i in range(count-1,len(line)):
	have=sorted([line[j] for j in range(i-(count-1),i+1)])
	good=1
	for j in range(count-1):
		if have[j]==have[j+1]:
			good=0
	if good:
		print(i+1)
		break