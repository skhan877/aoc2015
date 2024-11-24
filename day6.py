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
    
    # lit = 0
    on = []
    off = []

    for s in input:
        print(s)
        action, from_xy, to_xy = extract_action(s)
        if action == "on":
            print(from_xy, to_xy)
            on.append([(x, y) for x in range(int(from_xy[0]), int(to_xy[0]) + 1) for y in range(int(from_xy[1]), int(to_xy[1]) + 1)])
        print("")


    
    return on



def part_two(input):

    pass
    

def main():
    f = "inputs//day6.txt"
    data = parse_input(f)
    data = data[:10]
    # print(data)

    sample = ['turn on 0,0 through 2,2']

    print(part_one(sample))
    # print(part_two(data))


if __name__ == "__main__":
    main()