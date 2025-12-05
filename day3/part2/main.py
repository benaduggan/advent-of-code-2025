import sys


def main():
    result = 0
    inputFileName = "test-input.txt"
    if len(sys.argv) == 2 and sys.argv[1] == "full":
        inputFileName = "final-input.txt"

    with open(inputFileName, "r") as file:
        for line in file.readlines():
            print(line)

    print(f"ANSWER: {result}")


main()
