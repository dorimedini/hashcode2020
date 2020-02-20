import numpy as np


def line_to_int_tuple(line):
    return (int(x) for x in line.strip().split(' '))


def parse(filename):
    result = {
        'B': None,
        'L': None,
        'D': None,
        'scores': None,
        'books_in_library': [],
        'signup_time_for_library': [],
        'books_per_day_from_lib': [],
        'book_ids_for_library': [],
        'books_to_libraries_containing': {}
    }
    with open(filename, 'r') as file:
        result['B'], result['L'], result['D'] = line_to_int_tuple(file.readline())
        result['scores'] = list(line_to_int_tuple(file.readline()))
        for libID in range(result['L']):
            Nj, Tj, Mj = line_to_int_tuple(file.readline())
            result['books_in_library'].append(Nj)
            result['signup_time_for_library'].append(Tj)
            result['books_per_day_from_lib'].append(Mj)
            books_in_lib = list(line_to_int_tuple(file.readline()))
            result['book_ids_for_library'].append(books_in_lib)
            for book in books_in_lib:
                if book not in result['books_to_libraries_containing']:
                    result['books_to_libraries_containing'][book] = []
                result['books_to_libraries_containing'][book].append(libID)
        return result
