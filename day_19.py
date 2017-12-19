input = []

# Read all input
for line in open('input_test_19.txt'):
	input.append(line)
	
# Find the starting position
def find_start(input):
	for y, line in enumerate(input):
		for x, char in enumerate(line):
			if char != " ":
				return([x, y])

x, y = find_start(input)

index = 0			
directions = [[0,1], [1,0], [-1, 0], [0, -1]]

result = ""
next = True
while next:
	next = False
	for _ in range(4):
		#print(directions[index])
		xx = x + directions[index][0]
		yy = y + directions[index][1]
		
		print([[x,y], [xx, yy]])
		
		c = input[yy][xx]
		
		if c != " ":
			if c != "-" and c != "|" and c != "+":
				print(c)
				result = result + c
			x = xx
			y = yy
			next = True
			break;
			
		index = (index + 1) % 4

print(result)