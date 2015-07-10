# acm.timus.ru
# 1001 Reverse Root
import math
import sys

inp = []
for line in sys.stdin:
    inp.extend(line.split())

# output roots in reverse
for num in reversed(inp):
    out = math.pow(float(num), 0.5)
    print("{0:.4f}".format(out))
