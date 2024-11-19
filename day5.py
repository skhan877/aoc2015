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
    
    from collections import Counter

    nice_strings = []

    for strng in input:
        # print(strng)
        n = len(strng)
        if n < 3:
            continue

        pairs = [strng[0]+strng[1]]

        i, j = 1, 2
        while j < n:
            # rule 1
            if strng[i]+strng[j] != pairs[-1]:
                pairs.append(strng[i]+strng[j])
                i += 1
                j += 1
            else:
                i += 2
                j += 2
        
        pairs_count = 0
        cnter = Counter(pairs)
        for k, v in cnter.items():
            if v >= 2:
                pairs_count += 1
        
        trio = 0

        p, q, r = 0, 1, 2
        while r < n:
            # rule 2 
            if strng[p] == strng[r]:
                # print("valid trio", strng[p], strng[q], strng[r])
                trio += 1
            p += 1
            q += 1
            r += 1

        if pairs_count >= 1 and trio >= 1:
            nice_strings.append(strng)
        
        # print('')
    
    return len(nice_strings)


def main():
    f = "inputs//day5.txt"
    data = parse_input(f)
    # print(data)

    # sample1 = ['qjhvhtzxzqqjkmpb', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']
    sample2 = ['uurcxstgmygtbstg', 'qjhvhtzxzqqjkmpb', 'xxyxx', 'ieodomkazucvgmuy', 'aaa']

    # print(part_one(data))
    print(part_two(sample2))


if __name__ == "__main__":
    main()

