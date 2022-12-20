import json


def task():
    filename = "input.json"
    with open(filename) as file_:
        dicts = json.load(file_)

    gen_exr = (item["contains_improvement_appeals"] for item in dicts) # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
