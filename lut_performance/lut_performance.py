from datetime import datetime
from collections import OrderedDict
import timeit

import numpy as np

from cLut_performance import run_time_test as cRun_time_test


def run_time_test():
    runtimes = OrderedDict()
    run_count = 10000
    repeat = 3

    d = dict(zip([(x, y) for x in range(34) for y in range(34)], range(34 * 34)))
    positions = d.keys()
    block_positions = positions[:]
    rand_state = np.random.RandomState()
    rand_state.shuffle(block_positions)
    total = 0

    for r in range(repeat):
        total = 0
        start = datetime.now()
        for run_count in range(10000):
            for p in block_positions: total += d[p]
        end = datetime.now()
        runtimes.setdefault('lut', {})[r] = (end - start).total_seconds()

    for r in range(repeat):
        total = 0
        start = datetime.now()
        for run_count in range(10000):
            for p in block_positions: total += p[0] * 34 + p[1]
        end = datetime.now()
        runtimes.setdefault('calc', {})[r] = (end - start).total_seconds()

    runtimes['lut'] = min(runtimes['lut'].values())
    runtimes['calc'] = min(runtimes['calc'].values())
    return runtimes
