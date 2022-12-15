f=open("input.txt","r")
s=[]
for line in f:
	line=line[0:-1].split()
	sensor=[int(line[2][2:-1]),int(line[3][2:-1])]
	beacon=[int(line[8][2:-1]),int(line[9][2:])]
	s.append([sensor,beacon])
Y=2000000

def dist(p,q):
	return abs(p[0]-q[0])+abs(p[1]-q[1])

rg=[]

ans=0
for c in s:
	r=dist(c[0],c[1])
	d=abs(c[0][1]-Y)
	# print(c[0],c[1],2*(r-d)+1)
	if d>r:
		continue
	# ans+=2*(r-d)+1
	# ans-=int(c[1][1]==Y)
	rg.append([c[0][0]-(r-d),c[0][0]+(r-d)])
	# print(dist(c[0],c[1]))

N=int(5e7)
O=int(1e6)
res=[0 for i in range(N)]
for i in rg:
	for j in range(i[0]+O,i[1]+O+1):
		res[j]=1
for c in s:
	if c[1][1]==Y:
		res[c[1][0]+O]=0
ans+=sum(res)
print(ans)