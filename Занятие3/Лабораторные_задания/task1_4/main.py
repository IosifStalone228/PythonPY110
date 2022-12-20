INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, "w") as file:
        with open(INPUT_FILE, "r") as file2:
            for line in file2:
                line = line.upper()
                sline = line.strip()
                file.write(sline+'\n')


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
