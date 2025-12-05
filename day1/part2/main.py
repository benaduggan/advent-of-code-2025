import sys


def main():
    location = 50
    count = 0
    inputFileName = "test-input.txt"
    if len(sys.argv) == 2 and sys.argv[1] == "full":
        inputFileName = "final-input.txt"

    with open(inputFileName, "r") as file:
        for line in file.readlines():
            instruction = line.strip()
            direction = instruction[0]
            amount = int(instruction[1:])
            print(f"\n\n\nLOCATION: {location}")
            print(f"DIRECTION: {direction} -- AMOUNT: {amount}")

            new_value = location
            full_rotations = amount // 100
            if direction == "L":
                new_value = location - (amount % 100)
                if new_value < 0:
                    new_value = 100 + new_value
                    if new_value != 0 and location != 0:
                        print(f"COUNTED! old: {count} -- new {count + 1}")
                        count += 1
                if new_value > 99:
                    new_value = new_value - 99
                    if new_value != 0 and location != 0:
                        print(f"COUNTED! old: {count} -- new {count + 1}")
                        count += 1
            if direction == "R":
                new_value = location + (amount % 100)
                if new_value < 0:
                    new_value = 100 + new_value
                    if new_value != 0 and location != 0:
                        print(f"COUNTED! old: {count} -- new {count + 1}")
                        count += 1
                if new_value > 99:
                    new_value = new_value - 100
                    if new_value != 0 and location != 0:
                        print(f"COUNTED! old: {count} -- new {count + 1}")
                        count += 1

            print(new_value)
            location = new_value
            print(f"NEW LOCATION: {location}")
            if location == 0:
                print(f"COUNTED! old: {count} -- new {count + 1}")
                count += 1
            count += full_rotations
            if full_rotations > 0:
                print(f"ADDED EXTRA ROTATIONS: {full_rotations} -- NEW_VALUE {count}")
            full_rotations = 0

    print(f"ANSWER: {count}")


main()
