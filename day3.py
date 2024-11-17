def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    return arr       


def part_one(input):

    visited = [[0,0]]

    for move in input[0]:
        prev = visited[-1]
        if move == "^":    
            curr = [prev[0], prev[1] + 1]
        elif move == "v":
            curr = [prev[0], prev[1] - 1]
        elif move == ">":
            curr = [prev[0] + 1, prev[1]]
        elif move == "<":
            curr = [prev[0] - 1, prev[1]]
        
        if curr not in visited:
            visited.append(curr)

    return len(visited)


def part_two(input):
    
    pass


def main():
    f = "inputs//day3.txt"
    data = parse_input(f)
    # print(data[:10])

    print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()
