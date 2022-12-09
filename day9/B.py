f=open("input.txt","r")
d={'U':[0,1],'D':[0,-1],'R':[1,0],'L':[-1,0]}
head=[[0,0] for i in range(10)]
NAX=100000

def go(c,m):
	return [c[0]+m[0],c[1]+m[1]]
def hsh(c):
	return (c[0]+NAX)*NAX + (c[1]+NAX)
def follow(h,t):
	[dx,dy]=[(h[0]-t[0]),(h[1]-t[1])]
	if abs(dx)<=1 and abs(dy)<=1:
		return [t[0],t[1]]
	[mx,my]=[0 if dx==0 else dx//abs(dx),0 if dy==0 else dy//abs(dy)]
	t[0]+=mx
	t[1]+=my
	return [t[0],t[1]]

vis={}
vis[hsh([0,0])]=1

for line in f:
	[move,ct]=[d[line[0]],int(line[2:len(line)-1])]
	nex=[[0,0] for i in range(10)]
	for i in range(ct):
		nex[0]=go(head[0],move)
		for j in range(1,10):
			nex[j]=follow(nex[j-1],head[j])
		vis[hsh(nex[9])]=1
		head=nex

print(len(vis))