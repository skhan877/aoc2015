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
    data = "ckczppom"
    
    print(part_one(data))
    # print(part_two(data))


if __name__ == "__main__":
    main()
