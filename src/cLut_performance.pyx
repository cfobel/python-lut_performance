from datetime import datetime
from collections import OrderedDict

import numpy as np


cdef inline lookup_0(d, block_positions):
    cdef int total = 0
    for p in block_positions:
        total += d[p]


cdef inline calc_0(d, block_positions):
    cdef int total = 0
    for p in block_positions:
        total += p[0] * 34 + p[1]


cdef inline float my_timeit(f, d, block_positions, int repeat, int run_count):
    cdef int r
    cdef int i

    runtimes = np.empty(repeat, dtype=float)
    for r in range(repeat):
        total = 0
        start = datetime.now()
        for i in range(run_count):
            if f == 'calc_0':
                calc_0(d, block_positions)
            elif f == 'lookup_0':
                lookup_0(d, block_positions)
            else:
                raise ValueError, 'Unknown f: %s' % f
        end = datetime.now()
        runtimes[r] = (end - start).total_seconds()
    return runtimes.min()


def run_time_test(run_count=10000, load_factor=1):
    cdef int total
    cdef int repeat = 3
    cdef int i

    runtimes = OrderedDict()

    d = dict(zip([(x, y) for x in range(34) for y in range(34)], range(34 * 34)))

    positions = d.keys()
    block_positions = positions[:]
    rand_state = np.random.RandomState()
    rand_state.shuffle(block_positions)

    runtimes['lut'] = my_timeit('lookup_0', d, block_positions, repeat,
                                load_factor * run_count)
    runtimes['calc'] = my_timeit('calc_0', d, block_positions, repeat,
                                 load_factor * run_count)
    return runtimes
