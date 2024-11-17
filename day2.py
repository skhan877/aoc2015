def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    return arr       


def part_one(input):

    total = 0
    
    for dims in input:
        l, w, h = dims.replace("x", " ").split(" ")
        l, w, h = int(l), int(w), int(h)
        min_side = min(l*w, w*h, l*h)
        total += ((2 * l * w) + (2 * w * h) + (2 * l * h) + min_side)

    return total


def part_two(input):
    
    total = 0 

    for dims in input:
        l, w, h = dims.replace("x", " ").split(" ")
        l, w, h = int(l), int(w), int(h)
        vol = l * w * h 
        min_perim = 2 * min(l + w, w + h, l + h)
        total += (min_perim + vol)

    return total 


def main():
    f = "inputs//day2.txt"
    data = parse_input(f)
    # print(data[:10])

    print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()
