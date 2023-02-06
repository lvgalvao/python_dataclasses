# from itertools import chain

def chain(*iterables):
    for iterable in iterables:
        for value in iterable:
            yield value