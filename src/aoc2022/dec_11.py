import copy
import os


def get_inspections(monkeys):
    inspections = [monkeys[m]["inspected"] for m in monkeys]
    inspections.sort(reverse=True)
    return inspections


def print_monkey_items(monkeys, inspection_round):
    print(f"After round {inspection_round}:")
    for m in range(len(monkeys)):
        # print(f"Monkey {m} holds {monkeys[m]['items']}")
        print(f"  Monkey {m} did {monkeys[m]['inspected']} inspections")
    print()


def parse_input(lines):
    monkeys = {}
    for i in range(0, len(lines), 7):
        monkey = i // 7
        items = [int(item) for item in lines[i+1].split(": ")[1].split(", ")]
        operation = eval("lambda old:"+lines[i+2].split("=")[1])
        divisible = int(lines[i+3].split()[-1])
        test_true = int(lines[i+4].split()[-1])
        test_false = int(lines[i+5].split()[-1])
        monkeys[monkey] = {
            "items": items,
            "operation": operation,
            "divisible": divisible,
            "testTrue": test_true,
            "testFalse": test_false,
            "inspected": 0
        }
    return monkeys


def main(input_file):
    with open(input_file) as file:
        monkeys = parse_input(file.readlines())
    # part 1
    monkey_business(copy.deepcopy(monkeys), 20, lambda x: x // 3)
    # part 2
    truncator = 1
    for m in monkeys:
        truncator *= monkeys[m]["divisible"]
    monkey_business(copy.deepcopy(monkeys), 10000, lambda x: x % truncator)


def monkey_business(monkeys, rounds, worry_level):
    for r in range(rounds):
        for m in range(len(monkeys)):
            for item in monkeys[m]["items"]:
                monkeys[m]["inspected"] += 1
                new = monkeys[m]["operation"](item)
                new = worry_level(new)
                to_monkey = monkeys[m]["testTrue"] if (new % monkeys[m]["divisible"]) == 0 else monkeys[m]["testFalse"]
                monkeys[to_monkey]["items"].append(new)
            monkeys[m]["items"] = []
        print_monkey_items(monkeys, r + 1)
    inspections = get_inspections(monkeys)
    print(f"Most active monkeys inspected {inspections[0]} and {inspections[1]} items, monkey business is "
          f"{inspections[0] * inspections[1]}")


if __name__ == '__main__':
    main(os.path.dirname(__file__) + '/../../inputs/dec_11_input.txt')
