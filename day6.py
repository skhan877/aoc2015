def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    return arr


def part_one(input, size=1000):

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
    
    def matrix_sum(M):
        tot = 0 
        for row in M:
            for item in row:
                tot += item
        return tot 
    
    board = [[0] * size for rows in range(size)]

    for s in input:
        action, from_xy, to_xy = extract_action(s)
        coords = [[x, y] for x in range(int(from_xy[0]), int(to_xy[0]) + 1) for y in range(int(from_xy[1]), int(to_xy[1]) + 1)]

        if action == "on":
            for c in coords:
                board[c[0]][c[1]] = 1
        
        elif action == "off":
            for c in coords:
                board[c[0]][c[1]] = 0
        
        elif action == "toggle":
            for c in coords:
                board[c[0]][c[1]] = (board[c[0]][c[1]] - 1) % 2

    return matrix_sum(board)


def part_two(input, size=1000):

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
    
    def matrix_sum(M):
        tot = 0 
        for row in M:
            for item in row:
                tot += item
        return tot 
    
    board = [[0] * size for rows in range(size)]

    for s in input:
        # print(s)
        action, from_xy, to_xy = extract_action(s)
        coords = [[x, y] for x in range(int(from_xy[0]), int(to_xy[0]) + 1) for y in range(int(from_xy[1]), int(to_xy[1]) + 1)]

        if action == "on":
            for c in coords:
                board[c[0]][c[1]] += 1
        
        elif action == "off":
            for c in coords:
                if board[c[0]][c[1]] > 0:
                    board[c[0]][c[1]] -= 1
        
        elif action == "toggle":
            for c in coords:
                board[c[0]][c[1]] += 2

    return matrix_sum(board)

    

def main():
    f = "inputs//day6.txt"
    data = parse_input(f)
    # data = data[:4]
    # print(data[:4])

    sample = ['toggle 1,2 through 2,2'
              ,'turn on 0,0 through 2,2'
              , 'turn off 1,0 through 2,2'
              , 'turn on 2,2 through 3,3'
              , 'turn off 0,0 through 0,1'
              , 'toggle 0,0 through 1,1'
              ]

    # print(part_one(data, size=1000))
    print(part_two(data, size=1000))



if __name__ == "__main__":
    main()