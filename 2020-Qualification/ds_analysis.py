"""
B:

100K books, 1K libraries, 1K days.

All books have same score.
Each library has a DISJOINT set of 1K books.
Each library can ship one at a time.

Solution:
sort in increasing order of signup time, sign them up and go. The rest doesn't matter.
"""


"""
C:

100K books, 10K libraries, 100K days.

Book scores are in [1,600] with mean 300.76 (possibly uniform).

Between 10 and 20 books per library - which means (unless many books are missing) on average each book
exists in one or two libraries.

Signup time between 10 and 1000 days, average 506.07 (uniform?)

BOOKS PER DAY: AT LEAST 210!!
This means once a library is signed up, all it's books can be sent in a day.

Scores in library (sum of scores of books in a library) are between 1206 and 8093, with
an average of 4520.91 and variance 1160.35. This is low variance so we should probably
look at high-scoring libraries first.

Suggested solution:
Sort by (lib_score/lib_signup), highest goes first.
"""



"""
D:


"""

from input_parser import parse
import numpy as np
import math
from utils import total_library_scores


def minmax_avgvar(l):
    return min(l), max(l), np.average(l), math.sqrt(np.var(l))


def print_mmav(what_is_this, l):
    print("{} between {} and {}, avg is {} var is {}".format(what_is_this, *minmax_avgvar(l)))


def analyze(dataset):
    print_mmav("book scores", dataset['scores'])
    print_mmav("num of books", dataset['books_in_library'])
    print_mmav("days until signup", dataset['signup_time_for_library'])
    print_mmav("books per day", dataset['books_per_day_from_lib'])
    print_mmav("scores in library", total_library_scores(dataset))


b = parse('inputs/b_read_on.txt')
print(b['books_per_day_from_lib'])
print(b['signup_time_for_library'])
print(set(b['scores']))

print()
analyze(parse('inputs/c_incunabula.txt'))
print()
analyze(parse('inputs/d_tough_choices.txt'))
