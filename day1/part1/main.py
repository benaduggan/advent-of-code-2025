def main():
	print("hello world!")
	with open('test-input.txt', 'r') as file:
		for line in file.readlines():
			print(line.strip())

main()
