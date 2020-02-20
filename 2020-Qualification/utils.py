import numpy as np


def total_library_scores(dataset):
    r = []
    for l in range(dataset['L']):
        scores = np.array([dataset['scores'][bID] for bID in dataset['book_ids_for_library'][l]])
        r.append(np.sum(scores))
    return r
