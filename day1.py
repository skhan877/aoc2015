
def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line)

    return arr 


def main(): 
    f = "inputs//day1.txt"
    print(parse_input(f))


if __name__ == "__main__": 
    main() 

