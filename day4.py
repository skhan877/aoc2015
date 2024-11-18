def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    return arr       


def part_one(input):

    import hashlib 

    for i in range(1000000000):
        hsh = hashlib.md5((input+str(i)).encode("utf-8")).hexdigest()
        if hsh[:5] == "00000":
            return i, hsh 


def part_two(input):
    
    import hashlib 

    for i in range(1000000000):
        hsh = hashlib.md5((input+str(i)).encode("utf-8")).hexdigest()
        if hsh[:6] == "000000":
            return i, hsh 


def main():
    data = "ckczppom"
    # print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()
