n = int(input())

already_said = False

for x in range(n):
	sentence = input()
	if "simon says" in sentence[0:12]:
		already_said = True
		
		answer = sentence[11:]
		print(answer)
	else:
		print()