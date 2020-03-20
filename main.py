import sys

def mapping(s1, s2):
    return len(set(zip(s1, s2))) == len(set(s1)) == len(set(s2))


args1 = str(sys.argv[1])
args2 = str(sys.argv[2])
print(str(mapping(args1, args2)))
