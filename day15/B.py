f=open("input.txt","r")
s=[]
for line in f:
	line=line[0:-1].split()
	sensor=[int(line[2][2:-1]),int(line[3][2:-1])]
	beacon=[int(line[8][2:-1]),int(line[9][2:])]
	s.append([sensor,beacon])

N=4000000
M=N
# print(s)

def dist(p,q):
	return abs(p[0]-q[0])+abs(p[1]-q[1])

def hsh(c):
	return c[0]*N + c[1]

def check(idx):
	c=s[idx]
	r=dist(c[0],c[1])
	print(idx,flush=True)
	poss=set()
	lef=max(0,c[0][1]-r-1)
	rit=min(N,c[0][1]+r+1)
	for y in range(lef,rit+1):
		cd=abs(y-c[0][1])
		req=r+1-cd

		if c[0][0]+req>=0 and c[0][0]+req<=M and y>=0 and y<=M:
			poss.add(hsh([c[0][0]+req,y]))
		if c[0][0]-req>=0 and c[0][0]-req<=M and y>=0 and y<=M:
			poss.add(hsh([c[0][0]-req,y]))
	for k in poss:
		pt=[k//N,k%N]
		good=1
		for c in s:
			r=dist(c[0],c[1])
			if dist(pt,c[0])<=r:
				good=0
		if good:
			print([k,"here"],flush=True)
	print(idx,"end",flush=True)
"""
	only one unvisited
	check radius?
"""

for i in range(len(s)):
	check(i)