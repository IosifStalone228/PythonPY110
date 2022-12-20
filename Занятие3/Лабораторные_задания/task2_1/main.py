import json


def task() -> str:
    dict_numbers = {}
    for i in range(1,11):
        dict_numbers[i] = i**2
    return json.dumps(dict_numbers, indent = 4)


if __name__ == "__main__":
    print(task())
