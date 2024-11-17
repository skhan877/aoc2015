def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    return arr 


def part_one(input):
    
    for dims in input:
        l, w, h = dims.replace("x", " ").split(" ")
        print(dims, l, w, h)


def part_two(input):
    pass 


def main():
    f = "inputs//day2.txt"
    data = parse_input(f)
    # print(data[:10])

    print(part_one(data[:10]))
    # print(part_two(data))


if __name__ == "__main__":
    main()
