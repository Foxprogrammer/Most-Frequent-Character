from collections import Counter

phr = input()
count = {i: phr.count(i) for i in phr}

def getlowercase():
    rk = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    res = dict([(key, val) for key, val in
                count.items() if key in rk])
    return res

def getuppercase():
    rs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    res1 = dict([(key, val) for key, val in
                 count.items() if key in rs])
    return res1

def Main():
    res = getlowercase()
    res1 = getuppercase()
    res2 = {res1.casefold(): v for res1, v in res1.items()}
    resf = Counter(res) + Counter(res2)
    resf1 = (max(resf.items(), key=lambda k: k[1]))
    print(resf1)

if __name__ == '__main__':
    Main()

#the program works just fine, but I need to be able to print multiple key vaules if I have multiple maxs#