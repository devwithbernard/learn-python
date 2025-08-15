from typing import Any


def extract_solutions(filename: str) -> list[dict]:
    def get_item(parts: list) -> dict[str, str | Any] | None:
        for _ in ("-", "+"):
            if _ in parts[1]:
                operand = _
                values = parts[1].split(_)
                item = {"name": parts[0], "values": values,
                        "operand": operand, "solution": parts[-1]}
                return item

    items = []

    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(";")
            item = get_item(parts)

            if item:
                items.append(item)

    return items


def process_data(filename: str) -> dict[str, list]:
    def check_case(item: dict, operand) -> bool:
        if operand == "+":
            return int(item['values'][0]) + int(item['values'][1]) == int(item['solution'])
        elif operand == "-":
            return int(item['values'][0]) - int(item['values'][1]) == int(item['solution'])
        return False

    items = extract_solutions(filename)

    right_solutions = []
    wrong_solutions = []

    for item in items:
        operand = item.get("operand")

        if check_case(item, operand):
            right_solutions.append(item)
        else:
            wrong_solutions.append(item)

    data = {"right_solutions": right_solutions, "wrong_solutions": wrong_solutions}

    return data


def filter_data(filename: str) -> None:
    data = process_data(filename)

    right_solutions = data["right_solutions"]
    wrong_solutions = data["wrong_solutions"]

    with open("right_solutions.csv", mode="w") as r_file:
        for rs in right_solutions:
            r_line = f"{rs['name']};{rs['values'][0]}{rs['operand']}{rs['values'][1]};{rs['solution']}\n"
            r_file.write(r_line)

    with open("wrong_solutions.csv", mode="w") as w_file:
        for ws in wrong_solutions:
            w_line = f"{ws['name']};{ws['values'][0]}{ws['operand']}{ws['values'][1]};{ws['solution']}\n"
            w_file.write(w_line)

    print("file filtered successfully!")


def main() -> None:
    filter_data("solutions.csv")


if __name__ == '__main__':
    main()
