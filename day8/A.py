# O(N*M) even tho its not req :)

def main():
	f=open("input.txt","r")
	g=[line[0:len(line)-1] for line in f]
	[n,m]=[len(g),len(g[0])]
	vis=[[0 for i in range(m)] for i in range(n)]

	def valid(row, col):
		return row>=0 and col>=0 and row<n and col<m

	def iterate(row, col, d):
		# d: [xstep, ystep]
		mx=-1
		while valid(row,col):
			if int(g[row][col])>mx:
				vis[row][col]=1
				mx=int(g[row][col])
			row+=d[0]
			col+=d[1]
			
	for i in range(n):
		iterate(i,0,[0,1])
		iterate(i,m-1,[0,-1])
	for i in range(m):
		iterate(0,i,[1,0])
		iterate(n-1,i,[-1,0])
	print(sum([sum(vis[i]) for i in range(n)]))

main()