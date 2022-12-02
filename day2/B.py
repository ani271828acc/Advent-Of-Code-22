res=0
f=open("input.txt","r")
pts=[1,2,3]
scr=[3,6,0]
for line in f:
	b=(ord(line[2])-ord('X')+2)%3
	a=ord(line[0])-ord('A')
	res+=scr[b]+pts[(a+b)%3]
print(res)