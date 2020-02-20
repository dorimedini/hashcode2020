from input_parser import parse
import numpy as np
from utils import initial_library_scores


def solve_c():
    res = parse("inputs/c_incunabula.txt")
    days = int(res['D'])
    books_num = int(res['B'])
    libraries_num = int(res['L'])
    books_scores = np.asarray(res['scores'])

    num_of_books_in_library = np.asarray(res['books_in_library'])
    signup_time_for_library = np.asarray(res['signup_time_for_library'])
    books_per_day_from_lib = np.asarray(res['books_per_day_from_lib'])
    book_ids_for_library = np.asarray(res['book_ids_for_library'])

    # Sort by (total_book_score/signup_time), then do greedy
    scores = np.array(initial_library_scores(res))
    # print([score[0] for score in scores])
    sorted_libs = np.flip(np.argsort([score[0] for score in scores]))
    # print(scores[sorted_libs[:10]])
    return sorted_libs, book_ids_for_library


solve_c()
