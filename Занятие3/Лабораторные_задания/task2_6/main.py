import json


def task():
    filename = "input.json"
    with open(filename) as f:
        dicts = json.load(f)

    return  sorted(dicts, key=lambda item: item["length"])


if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))

    # TODO дополнительно записать отсортированный список в JSON файл
