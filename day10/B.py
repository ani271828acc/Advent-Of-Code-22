def main():
	f=open("input.txt","r")
	[cyc,val,n,m,pos]=[1,1,40,6,0]
	cur=[]
	d=".#"

	def why():
		cur.append(int(abs(len(cur)-val)<2))
		if len(cur)==n:
			render(cur)
			cur=[]

	def render():
		for c in cur:
			print(d[c],end='')
		print()

	for line in f:
		if line[0]=='n':
			cur.append(int(abs(len(cur)-val)<2))
			if len(cur)==n:
				render()
				cur=[]
				cyc+=1
		else:
			cur.append(int(abs(len(cur)-val)<2))
			if len(cur)==n:
				render()
				cur=[]
				cyc+=1
			cur.append(int(abs(len(cur)-val)<2))
			if len(cur)==n:
				render()
				cur=[]
			val+=int(line[0:len(line)-1].split()[-1])

main()