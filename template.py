def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    return arr


def part_one(input):

    pass


def part_two(input):

    pass
    

def main():
    f = "inputs//day6.txt"
    data = parse_input(f)
    # print(data)
    # data = data[-20:]

    # sample = []

    # print(part_one(data))
    # print(part_two(data))


if __name__ == "__main__":
    main()