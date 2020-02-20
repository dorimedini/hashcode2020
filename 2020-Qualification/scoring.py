from utils import total_library_scores
import numpy as np
from input_parser import parse


def c_score(dataset):
    '''return the score for dataset c'''
    scores = np.array(total_library_scores(dataset))
    scores = scores/dataset['signup_time_for_library']
    return scores


def c_score_update(dataset, scores, library):
    return

c = parse('inputs/c_incunabula.txt')
