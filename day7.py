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
        # separate input and output
        instr = instr.split(" -> ")
        outp = instr[1]

        # split inputs
        inp = instr[0].split(" ")
        inp = [x.replace(x, str(signals[x])) if x in signals.keys() else x for x in inp]
        

        # add mappings to signals dict
        signals[outp] = inp[0] if len(inp) == 1 else inp
        print({outp: inp[0] if len(inp) == 1 else inp})

        print("")

    return signals


def part_two(input, size=1000):

    pass 



def main():
    f = "inputs//day7.txt"
    data = parse_input(f)
    # data = data[:6]
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
