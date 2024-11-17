
def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line)

    return arr 

def part_one(input):

    level = 0 

    for par in input[0]: 
        # print(par)
        if par == "(":
            level += 1
        elif par == ")":
            level -=1 

    return level 


def part_two(input): 

    instructions = input[0]
    n = len(instructions)
    level = 0 

    for i in range(n): 
        if instructions[i] == "(":
            level += 1
        elif instructions[i] == ")":
            level -=1 
        
        if level == -1:
            return i  + 1

    return -1


def main(): 
    f = "inputs//day1.txt"
    data = parse_input(f)
    # print(part_one(data))
    print(part_two(data))


if __name__ == "__main__": 
    main() 

