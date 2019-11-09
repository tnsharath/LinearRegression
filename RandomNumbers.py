import random
lowerLimitA, upperLimitA = 230, 250
lowerLimitB, upperLimitB = 300, 330 

file = open("outputRand.txt", "a")
counter = 1;
for i in range(1, 1000):
	if (counter%6 == 0) or (counter%7 == 0):
		file.write(str(random.randrange(lowerLimitB, upperLimitB)) + "\n")
	else:
		file.write(str(random.randrange(lowerLimitA, upperLimitA))+ "\n")
	if (i % 100 == 0):
		lowerLimitA, upperLimitA = lowerLimitA + 30, upperLimitA + 30
		lowerLimitB, upperLimitB = lowerLimitB + 30, upperLimitB + 30
	counter += 1;
	if counter == 8:
		counter = 1;
file.close()