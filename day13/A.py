f=open("input.txt","r")
lines=[eval(line[0:-1]) for line in f]
ans=0
for i in range(len(lines)//2):
	a=lines[2*i]
	b=lines[2*i+1]
	