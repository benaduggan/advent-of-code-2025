import sys


def main():
    result = 0
    inputFileName = "test-input.txt"
    if len(sys.argv) == 2 and sys.argv[1] == "full":
        inputFileName = "final-input.txt"

    with open(inputFileName, "r") as file:
        for line in file.readlines():
            for idRange in line.split(","):
                start = int(idRange.split("-")[0])
                end = int(idRange.split("-")[1])
                print(f"\n\n\nSTART {start} END: {end}")
                for i in range(start, end + 1):
                    valueString = str(i)
                    valueLength = len(valueString)
                    if valueLength % 2:
                        print("odd number of characters -- ignoring!")
                    else:
                        firstHalf = valueString[(valueLength // 2) :]
                        secondHalf = valueString[: (valueLength // 2)]
                        print(f"even number of characters {firstHalf} / {secondHalf}")
                        if firstHalf == secondHalf:
                            print(f"ADDING!")
                            result += i

    print(f"ANSWER: {result}")


main()
