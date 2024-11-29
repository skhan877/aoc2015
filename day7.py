def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    return arr


def part_one(input):

    signals = {} 

    for instr in input: 
        print(instr)
        instr = instr.split(" -> ")
        print(instr)
        print(instr[0].split(" "))
        print("")

    print(123 & 456)
    # print(6 >> 1)

    return signals 


def part_two(input, size=1000):

    pass 


# def convert_syntax(word): 

#     operators = {"AND": &,
#         "OR": |,
#         "XOR": ^,
#         "NOT": ~,
#         "RSHIFT": >>,
#         "LSHIFT": <<
#         }
    
#     return operators[word]


def main():
    f = "inputs//day7.txt"
    data = parse_input(f)
    # data = data[:4]
    # print(data[:4])

    sample = ['123 -> x',
            '456 -> y',
            'x AND y -> d',
            'x OR y -> e',
            'x LSHIFT 2 -> f',
            'y RSHIFT 2 -> g',
            'NOT x -> h',
            'NOT y -> i'
            ]

    print(part_one(sample))
    # print(part_two(data))





if __name__ == "__main__":
    main() 
