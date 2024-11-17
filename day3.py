def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    return arr       


def part_one(input):

    visited = [(0,0)]

    for move in input[0]:
        prev = visited[-1]
        # print(F"prev: {prev}")
        # print(f"move: {move}")
        if move == "^":    
            curr = (prev[0], prev[1] + 1)
        elif move == "v":
            curr = (prev[0], prev[1] - 1)
        elif move == ">":
            curr = (prev[0] + 1, prev[1])
        elif move == "<":
            curr = (prev[0] - 1, prev[1])
        visited.append(curr)
        # print(f"curr: {curr}")
        
    return len(set(visited))


def part_two(input):
    
    santa = [(0,0)]
    robot = [(0,0)]

    # santas moves
    for move in input[0][::2]:
        prev = santa[-1]
        if move == "^":    
            curr = (prev[0], prev[1] + 1)
        elif move == "v":
            curr = (prev[0], prev[1] - 1)
        elif move == ">":
            curr = (prev[0] + 1, prev[1])
        elif move == "<":
            curr = (prev[0] - 1, prev[1])
        santa.append(curr)

    # robots moves
    for move in input[0][1::2]:
        prev = robot[-1]
        if move == "^":    
            curr = (prev[0], prev[1] + 1)
        elif move == "v":
            curr = (prev[0], prev[1] - 1)
        elif move == ">":
            curr = (prev[0] + 1, prev[1])
        elif move == "<":
            curr = (prev[0] - 1, prev[1])
        robot.append(curr)

    # combined
    combined = set(santa + robot)
    return len(combined)


def main():
    f = "inputs//day3.txt"
    data = parse_input(f)
    # print(data)
    # sample = ["^v^v^v^v^v"]
    
    # print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()
