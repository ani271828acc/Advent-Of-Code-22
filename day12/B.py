from queue import Queue

f=open("input.txt","r")
g=[[ord(i) for i in line[0:-1]] for line in f]
[n,m,inf]=[len(g),len(g[0]),int(1e9+7)]
cost=[[inf for i in range(m)] for i in range(n)]
q=Queue()

def find(c,k):
	for i in range(n):
		for j in range(m):
			if g[i][j]==c:
				g[i][j]=k
				return [i,j]

[S,E,dr,dc]=[find(ord('S'),ord('a')),find(ord('E'),ord('z')),[1,-1,0,0],[0,0,1,-1]]
cost[S[0]][S[1]]=0
q.put(S)
for i in range(n):
	for j in range(m):
		if g[i][j]==ord('a'):
			cost[i][j]=0
			q.put([i,j])

while not q.empty():
	at=q.get()
	for d in range(4):
		[r,c]=[at[0]+dr[d],at[1]+dc[d]]
		if r<0 or c<0 or r>n-1 or c>m-1 or g[r][c]-g[at[0]][at[1]]>1:
			continue
		if cost[r][c]>cost[at[0]][at[1]]+1:
			cost[r][c]=cost[at[0]][at[1]]+1
			q.put([r,c])
print(cost[E[0]][E[1]])