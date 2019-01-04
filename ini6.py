import sys


def word_count(s):
    return {w: s.split(' ').count(w) for w in s.split(' ')}


def print_count(d):
    for w, c in d.items():
        print(w, c)
