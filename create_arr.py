with open('comments') as f:
	lines = f.readlines()

arr = []
tpl = []
n = 1

for line in lines:
	line = line.strip()

	if n == 2:
		tpl.append(line)
	elif n == 3:
		tpl.append(line.split())
	elif n == 5:
		arr.append(tpl)
		tpl = []
		n = 0

	n += 1

print (arr)
