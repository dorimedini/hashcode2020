from utils import parse_file
import numpy as np


def solve():
    (days, books_num, libraries_num, books_scores, num_of_books_in_library, signup_time_for_library,
     books_per_day_from_lib, book_ids_for_library) = parse_file("inputs/d_tough_choices.txt")
    sorted_libs = np.flip(np.argsort([len(x) for x in book_ids_for_library]))
    return (sorted_libs, book_ids_for_library, num_of_books_in_library, books_per_day_from_lib,
            days, signup_time_for_library)
