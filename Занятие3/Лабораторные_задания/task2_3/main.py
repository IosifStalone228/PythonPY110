import json


def task():
    filename = "input.json"
    with open(filename) as file_:
        dicts = json.load(file_)

    return  max(dicts, key=lambda item: item["score"])


if __name__ == "__main__":
    print(task())
