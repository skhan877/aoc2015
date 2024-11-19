def parse_input(input): 
    
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))

    return arr       


def part_one(input):

    vowels = ['a','e','i','o','u']
    disallowed = ['ab', 'cd', 'pq', 'xy']
    good_strings = []

    for strng in input: 

        vowel_count = 0
        dupe_count = 0
        disallowed_count = 0
        
        if strng[0] in vowels:
            vowel_count += 1
        
        for i in range(1, len(strng)):
            # rule 1
            if strng[i] in vowels:
                vowel_count += 1
            # rule 2
            if strng[i] == strng[i-1]:
                dupe_count += 1
            # rule 3
            if strng[i-1:i+1] in disallowed:
                disallowed_count += 1
        
        if vowel_count >= 3 and dupe_count >= 1 and disallowed_count == 0:
            good_strings.append(strng)

    return len(good_strings)


def part_two(input):
    
    pass


def main():
    f = "inputs//day5.txt"
    data = parse_input(f)
    # print(data)

    # sample = ['ugknbfddgicrmopn', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']

    print(part_one(data))
    # print(part_two(data))


if __name__ == "__main__":
    main()

