f=open("input.txt","r")
lines=[line[0:-1].split() for line in f]

class Monkey:
	def __init__(self,items,op,div,x,y):
		self.activity=0
		self.items=items
		self.op=op
		self.div=div
		self.to=[y,x]
	def inspect(self,old):
		self.activity+=1
		return eval(self.op)//3
	def turn(self):
		res=[self.inspect(i) for i in self.items]
		self.items.clear()
		return res
	def __str__(self):
		return str([self.items,self.op,self.div,self.to])

def process(monkeys, idx):
	res=monkeys[idx].turn()
	for i in res:
		to=monkeys[idx].to[int((i%monkeys[idx].div)==0)]
		monkeys[to].items.append(i)

monkeys=[]

for i in range(0,len(lines),7):
	items=[int(i.split(',')[0]) for i in lines[i+1][2:]]
	op="".join([i for i in lines[i+2][3:]])
	[div,x,y]=[int(lines[i+3][3]),int(lines[i+4][5]),int(lines[i+5][5])]
	monkeys.append(Monkey(items,op,div,x,y))

for i in range(20):
	for j in range(len(monkeys)):
		process(monkeys,j)

act=sorted([i.activity for i in monkeys])
print(act[-1]*act[-2])