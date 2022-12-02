res=0
f=open("input.txt","r")
pts=[1,2,3]
scr=[3,0,6]
for line in f:
	b=ord(line[2])-ord('X')
	a=ord(line[0])-ord('A')
	res+=pts[b]+scr[(a-b+3)%3]
print(res)