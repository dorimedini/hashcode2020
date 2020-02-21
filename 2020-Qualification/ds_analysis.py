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

Books/Libraries/Days: 78600,30000,30001
All books scores are 65.
All signup times are 2.
Each library can do one book per day.
Books per library in [1,14], avg 7.36 var 1.8
(previous stat implies scores are in [65,910]. Avg is 478.4, var 117)

Interesting:
Each book is contained in either 2 or 3 libraries exactly.
The variance on the number of books per library is low.
Seems like books are pretty evenly spread-out so I wouldn't expect a huge saving
in computing how libraries' score should go down due to previous selection of the
books already inside.

I would say:
Sort in descending order of books-per-library and do greedy.
"""



"""
E:

Books/Libraries/Days: 100000,1000,200
book scores between 1 and 250, avg is 125.48648 var is 72.02151718208664
num of books between 2 and 1000, avg is 491.942 var is 286.9493311300795
days until signup between 1 and 10, avg is 5.432 var is 2.898512722069717
books per day between 1 and 2, avg is 1.494 var is 0.4999639987039066
scores in library between 227 and 129651, avg is 61690.074 var is 36069.812571602364
Books missing from all libraries: 736
libraries containing a specific book: between 1 and 18, avg is 4.955895390070922 var is 2.180343502271195
Histogram of books-per-library: (array([ 97, 115,  92, 104, 103, 103, 110,  87,  99,  90], dtype=int32), 
        array([   2. ,  101.8,  201.6,  301.4,  401.2,  501. ,  600.8,  700.6,  800.4,  900.2, 1000. ]))
        
This seems hard.
Human-eye analysis: can't see any patterns other than the above stats.
Huge difference in both library scores and book scores.
However, we can afford D^3 runtime (even D^4) where D is the number of days.
The number of libraries is pretty low as well, and we can only choose 200 of them in the end.
How do we use this to our advantage?

Since time is a bottlneck here, maybe divide a libraries' score by signup_days**2 instead of just signup_days?
"""


"""
F:

Books/Libraries/Days: 100000,1000,700
book scores between 1 and 800, avg is 401.11142 var is 231.00251198976952
num of books between 1 and 1000, avg is 509.342 var is 289.6414490987089
days until signup between 30 and 300, avg is 166.192 var is 78.67589933391292
books per day between 5 and 10, avg is 7.467 var is 1.6955562509100075
scores in library between 164 and 412714, avg is 204421.248 var is 116574.11414030346
Books missing from all libraries: 575
libraries containing a specific book: between 1 and 17, avg is 5.122876540105607 var is 2.2257636464824415
Histogram of books-per-library: (array([ 93, 101,  84, 109, 107, 110,  84,  87, 124, 101], dtype=int32),
        array([   1. ,  100.9,  200.8,  300.7,  400.6,  500.5,  600.4,  700.3,  800.2,  900.1, 1000. ]))

Interesting:
Min signup-time of a library is 30 days and we only have 700 days, so at most 700//30=23 libraries can be chosen.
So: this is a question of finding the top ~20 libraries to sign up.
Also:
Note that for libraries with a 10-book-per-day rate, we need an average of 50 days to push out all the books in the
library.  
(Brute-forcing this is approximately 1000^23, the technical term for which is "bad")
"""

from input_parser import parse
import numpy as np
import math
from utils import total_library_scores, missing_books


def minmax_avgvar(l):
    return min(l), max(l), np.average(l), math.sqrt(np.var(l))


def print_mmav(what_is_this, l):
    print("{} between {} and {}, avg is {} var is {}".format(what_is_this, *minmax_avgvar(l)))


def analyze(dataset):
    print(f"Books/Libraries/Days: {dataset['B']},{dataset['L']},{dataset['D']}")
    print_mmav("book scores", dataset['scores'])
    print_mmav("num of books", dataset['books_in_library'])
    print_mmav("days until signup", dataset['signup_time_for_library'])
    print_mmav("books per day", dataset['books_per_day_from_lib'])
    print_mmav("scores in library", total_library_scores(dataset))
    print(f"Books missing from all libraries: {missing_books(dataset)}")
    print_mmav("libraries containing a specific book:",
               [len(dataset['books_to_libraries_containing'][book]) for book in dataset['books_to_libraries_containing']])
    print(f"Histogram of books-per-library: {np.histogram([len(ids) for ids in dataset['book_ids_for_library']])}")


print("B")
analyze(parse('inputs/b_read_on.txt'))
print("C")
analyze(parse('inputs/c_incunabula.txt'))
print()
analyze(parse('inputs/d_tough_choices.txt'))
print()
analyze(parse('inputs/e_so_many_books.txt'))
print()
analyze(parse('inputs/f_libraries_of_the_world.txt'))
