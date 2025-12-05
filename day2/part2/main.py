import re
import sys


def main():
    result = 0
    inputFileName = "test-input.txt"
    if len(sys.argv) == 2 and sys.argv[1] == "full":
        inputFileName = "final-input.txt"

    with open(inputFileName, "r") as file:
        for line in file.readlines():
            for idRange in line.split(","):
                if not idRange.strip():
                    break
                start = int(idRange.split("-")[0])
                end = int(idRange.split("-")[1])
                # print(f"\n\n\nSTART {start} END: {end}")
                for i in range(start, end + 1):
                    valueString = str(i)
                    matches = re.search(r"^\b(\d+)\1+$", valueString)
                    # print(f"matches for {i}: {matches}")
                    if matches:
                        # print(matches.groups())
                        result += i

    print(f"ANSWER: {result}")


main()
