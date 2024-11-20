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

    def two_pairs(s):
        for i in range(2, len(s)-1):
            a = s[i-2: i]
            b = s[i: ]
            if a in b:
                return True 
        return False
    
    def valid_trios(s):
        for i in range(len(s)-2):
            a = s[i]
            b = s[i+2]
            if a == b:
                return True 
        return False
    
    def is_nice(s):
        return two_pairs(s) and valid_trios(s)

    nice_strings = 0 

    for strng in input:
        # print(strng)
        if is_nice(strng):
            nice_strings += 1

    return nice_strings
    

def main():
    f = "inputs//day5.txt"
    data = parse_input(f)
    # print(data)
    # data = data[-20:]

    # sample = ['qjhvhtzxzqqjkmpb', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']
    # sample = ['uurcxstgmygtbstg', 'qjhvhtzxzqqjkmpb', 'xxyxx', 'ieodomkazucvgmuy', 'aaa']
    # sample = ['xckozymymezzarpy', 'cxoaaphylmlyljjz', 'ionndmdwpofvjnnq', 'ywehopujowckggkg', 'cekjbablkjehixtj', 'ycsfscegcexcnbwq', 'qpjdsocrtwzpjdkd', 'jdckfjdtjsszdzhj', 'yohdmucunrgemqcu', 'xvgpghhdtpgvefnk', 'iiewevdzbortcwwe', 'twichytatzoggchg', 'qmgvroqwrjgcycyv', 'ezvjijcjcyszwdjy', 'dodjadoqyxsuazxt', 'jswabfbzpnhhdbpn', 'yjdjeckmsrckaagx', 'avdtdppodpntojgf', 'hoyqdzofddedevsb', 'bubeonwbukprpvhy', 'romyflhrarxchmyo', 'jfhobjxionolnouc', 'lfgehftptlfyvvaj', 'pkldomvvklefcicw', 'arerrohyhhkmwhyo', 'pvcvcsupfwsmeacs', 'gqgqyjvqmfiwiyio', 'eygyuffeyrbbhlit', 'jrcrdjrvsyxzidsk', 'njgolfwndqnwdqde', 'rurtxgibkeaibofs', 'sfrwfazygygzirwd', 'yccaifzmvbvwxlcc', 'szephmeegvegugdt', 'dtuhjnlaliodtlvh', 'vjqkhkhjlmvpwkud', 'hsvikeyewfhsdbmy', 'aapqpwapzyjnusnr', 'xckvsnkvnvupmirv', 'oyzhmirzrnoytaty', 'rpepcfpelvhzzxzj', 'lmfiylebtzwtztmx', 'uyibwcitxixjfwcr', 'yktkmkokmfslgkml', 'icdawnmfnpnmyzof', 'fgysnxrnfnxprdmf', 'mqzxvvskslbxvyjt', 'qryjbohkprfazczc', 'hubpbvxknepammep', 'gthxhaapfpgtilal']

    # print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()

