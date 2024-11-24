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
        # print(s)
        action, from_xy, to_xy = extract_action(s)
        coords = [(x, y) for x in range(int(from_xy[0]), int(to_xy[0]) + 1) for y in range(int(from_xy[1]), int(to_xy[1]) + 1)]
        if action == "on":
            # print("on", coords)
            on += [c for c in coords if c not in on]
        elif action == "off":
            # print("off", coords)
            on = [c for c in on if c not in coords]
        elif action == "toggle":
            # print("toggle", coords)
            for c in coords:
                if c in on:
                    on.remove(c)
                elif c not in on:
                    on += [c]
        
        # print("currently on: ", on)
        # print("")

    return len(on)



def part_two(input):

    pass
    

def main():
    f = "inputs//day6.txt"
    data = parse_input(f)
    data = data[:4]
    print(data[:4])

    sample = ['toggle 1,2 through 2,2'
              ,'turn on 0,0 through 2,2'
              , 'turn off 1,0 through 2,2'
              , 'turn on 2,2 through 3,3'
            #   , 'turn off 0,0 through 0,1'
              , 'toggle 0,0 through 1,1'
              ]

    # print(part_one(data))
    # print(part_two(data))

    '''
    TODO: create matrix and update elements to 1 or 0 then sum elements
    '''


if __name__ == "__main__":
    main()