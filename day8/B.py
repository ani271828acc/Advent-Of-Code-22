# O(N*M) even tho its not req :)

def main():
	f=open("input.txt","r")
	g=[line[0:len(line)-1] for line in f]
	[n,m]=[len(g),len(g[0])]
	vis=[[1 for i in range(m)] for i in range(n)]

	def valid(row, col):
		return row>=0 and col>=0 and row<n and col<m

	def iterate(row, col, d):
		# d: [xstep, ystep]
		stack=[[10,0]]
		i=0
		while valid(row,col):
			while stack[-1][0]<int(g[row][col]):
				stack.pop()
			vis[row][col]*=(i-stack[-1][1])
			stack.append([int(g[row][col]),i])
			[row,col,i]=[row+d[0],col+d[1],i+1]
			
	for i in range(n):
		iterate(i,0,[0,1])
		iterate(i,m-1,[0,-1])
	for i in range(m):
		iterate(0,i,[1,0])
		iterate(n-1,i,[-1,0])
	print(max([max(vis[i]) for i in range(n)]))

main()