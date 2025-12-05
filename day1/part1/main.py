import sys


def main():
    location = 50
    count = 0
    inputFileName = "test-input.txt"
    if len(sys.argv) == 2 and sys.argv[1] == "full":
        inputFileName = "final-input.txt"

    with open(inputFileName, "r") as file:
        for line in file.readlines():
            print()
            instruction = line.strip()
            direction = instruction[0]
            amount = int(instruction[1:])
            print(direction)
            print(amount)

            new_value = location
            if direction == "L":
                new_value = location - (amount % 100)
                if new_value < 0:
                    new_value = 100 + new_value
                if new_value > 99:
                    new_value = new_value - 99

            if direction == "R":
                new_value = location + (amount % 100)
                if new_value < 0:
                    new_value = 100 + new_value
                if new_value > 99:
                    new_value = new_value - 100

            print(new_value)
            location = new_value
            if location == 0:
                count += 1

    print(f"ANSWER: {count}")


main()
