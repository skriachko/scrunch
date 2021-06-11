#
# Generates all possible password combinations from character set.
#
# Author: Sergii Kriachko <sk@topdev.se>
#
# Example 1:
# Generate all combinations from charset "ABCDEFGH123456"
#  excluding "ABC" substring. Each symbol can occur only once.
#  Print results to STDOUT.
#
#  python3 word.py --no-rep -ex ABC 3 5 ABCDEFGH123456
#
# Example 2:
#  Generate all combinations from charset that includes:
#  - all uppercase letters
#  - all lowercase letters
#  - all decimal digits
#  with length of 6 symbols.
#  Each symbol can occur only once.
#  Print results to file wordlist.txt.
#
#  python3 word.py --no-rep -f wordlist.txt -u -l -d 6 6
#

import string
import argparse
import itertools
from math import factorial

parser = argparse.ArgumentParser(description='Generate password combinations from charset'
'with length in range: [MIN..MAX]. '
'If any of -u, -l, -d, -hex option is set, then charset is ignored, but still must be provided.')

parser = argparse.ArgumentParser(epilog="Example 1: "
'python3 word.py --no-rep -ex ABC 3 5 ABCDEFGH123456 '
'Example 2: '
'python3 word.py --no-rep -f wordlist.txt -u -l -d 6 6 DUMMYCHARSET')

parser.add_argument('-f', metavar='file', help='output text file name. Prints to STDOUT by default')
parser.add_argument('-u', action='store_true', help='Use all uppercase characters. Overrides charset')
parser.add_argument('-l', action='store_true', help='Use all lowercase characters. Overrides charset')
parser.add_argument('-d', action='store_true', help='Use all decimal numbers. Overrides charset')
parser.add_argument('-hex', action='store_true', help='Use all hex numbers. Overrides charset')
parser.add_argument('-ex', metavar='exclude', help='Exclude char sequence')
parser.add_argument('--no-digit-start', action='store_true', help='Do not start with digit')
parser.add_argument('minlen', metavar='MIN', type=int,
                    help='Min length of combination')
parser.add_argument('maxlen', metavar='MAX', type=int,
                    help='Max length of combination')
parser.add_argument('charset', nargs=1)
parser.add_argument('--no-rep', action='store_true', help='Any symbol can occur only once.')

args = parser.parse_args()

def number_permutations(n, k):
 return factorial(n)/factorial(n-k)


def permutations_no_digit_start(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                if pool[indices[0]].isdigit():
                 continue
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

a = ''.join(args.charset)
b = ''
if args.u:
 b += string.ascii_uppercase
if args.l:
 b += string.ascii_lowercase
if args.hex:
 b += string.hexdigits
if args.d:
 b += string.digits

if b:
  a = b


s = sorted(a)
print (s)
num = 0
# Calculate number of possible combinations
for L in range(args.minlen, args.maxlen + 1):
 num += number_permutations(len(s), L)
print ("Number of combinations: %d" % num)

if args.f:
 f = open(args.f, 'w')

for L in range(args.minlen, args.maxlen + 1):
 if args.no_digit_start and args.no_rep:
  gen = permutations_no_digit_start(s, L)
 elif args.no_rep:
  gen = itertools.permutations(s, L)
 else:
  gen  = itertools.product(s, repeat=L)
 for x in gen:
  y = ''.join(x)
  if args.ex and args.ex in y:
   continue
  if args.no_digit_start and y[0].isdigit():
   continue
  if args.f:
   f.write("%s\n" % ''.join(x))
  else:
   print (''.join(x))


