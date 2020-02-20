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
        'book_ids_for_library': []
    }
    with open(filename, 'r') as file:
        result['B'], result['L'], result['D'] = line_to_int_tuple(file.readline())
        result['scores'] = list(line_to_int_tuple(file.readline()))
        for libID in range(result['L']):
            Nj, Tj, Mj = line_to_int_tuple(file.readline())
            result['books_in_library'].append(Nj)
            result['signup_time_for_library'].append(Tj)
            result['books_per_day_from_lib'].append(Mj)
            result['book_ids_for_library'].append(list(line_to_int_tuple(file.readline())))
        return result
