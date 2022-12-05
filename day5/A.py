f=open("input.txt", "r")
lines=[]
for line in f:
	lines.append(line[0:len(line)-1])
tc=(len(lines[0])+1)//4
towers=[[] for i in range(tc)]


for j in range(len(lines)):
	line=lines[j]
	if line[0]==' ':
		lines=lines[j+2:]
		break
	for i in range(tc):
		if line[4*i+1]!=' ':
			towers[i].append(line[4*i+1])

for tower in towers:
	tower.reverse()

for line in lines:
	line=line.split(' ')
	e=[int(line[1]),int(line[3]),int(line[5])]
	while e[0]:
		towers[e[2]-1].append(towers[e[1]-1].pop())
		e[0]-=1
for tower in towers:
	print(tower.pop(),end='')