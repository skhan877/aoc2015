def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    return arr


def part_one(input):

    def extract_action(s):
        if 'turn on' in s:
            action = 'on'
            coords = s.replace('turn on ', '').split(' through ')
            from_xy, to_xy = coords[0], coords[1]
        elif 'turn off' in s:
            action = 'off'
            coords = s.replace('turn off ', '').split(' through ')
            from_xy, to_xy = coords[0], coords[1]
        elif 'toggle' in s:
            action = 'toggle'
            coords = s.replace('toggle ', '').split(' through ')
            from_xy, to_xy = coords[0], coords[1]

        return (action, from_xy.split(','), to_xy.split(','))
    
    for s in input:
        print(extract_action(s))


def part_two(input):

    pass
    

def main():
    f = "inputs//day6.txt"
    data = parse_input(f)
    data = data[-20:]
    # print(data)

    # sample = []

    print(part_one(data))
    # print(part_two(data))


if __name__ == "__main__":
    main()