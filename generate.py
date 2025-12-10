with open("artifact.txt", "w") as f:
	for i in range(100_000):
		print(i, file=f)
print("<3")
