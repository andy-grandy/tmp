import argparse

parser = argparse.ArgumentParser(description='Short sample app')
parser.add_argument('-a', type=int, action="store", dest="a", help='Store a constant value')
parser.add_argument('-b', type=int, action="store", dest="b", help='Store a constant value')

args = parser.parse_args()
print("A=%s B=%s SUM=%s")%(args.a, args.b, args.a+args.b)
