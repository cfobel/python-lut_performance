from datetime import datetime
from collections import OrderedDict
import timeit

import numpy as np

from cLut_performance import run_time_test as cRun_time_test


def run_time_test(run_count=10000, load_factor=1):
    runtimes = OrderedDict()
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
        for i in range(run_count * load_factor):
            for p in block_positions: total += d[p]
        end = datetime.now()
        runtimes.setdefault('lut', {})[r] = (end - start).total_seconds()

    for r in range(repeat):
        total = 0
        start = datetime.now()
        for i in range(run_count * load_factor):
            for p in block_positions: total += p[0] * 34 + p[1]
        end = datetime.now()
        runtimes.setdefault('calc', {})[r] = (end - start).total_seconds()

    runtimes['lut'] = min(runtimes['lut'].values())
    runtimes['calc'] = min(runtimes['calc'].values())
    return runtimes


def main():
    print 'Runtimes'
    run_count = 10000
    print '  Python:', ', '.join(['%s: %s seconds' % (k, v)
                                  for k, v in run_time_test(run_count).items()])

    run_time = min(timeit.repeat(
        'd = dict(zip([(x, y) for x in range(34) '\
        'for y in range(34)], range(34 * 34)))', number=run_count))
    print 'Runtime to create lookup table:', run_time

    results = OrderedDict([(1 << r, cRun_time_test(run_count, 1 << r).items())
                           for r in range(5)])
    result_strs = [(label, ', '.join(['%s: %s seconds' % (k, v) for k, v in r]))
                   for label, r in results.iteritems()]
    print '\n'.join(['    [load factor %3d] %s' % item for item in result_strs])


if __name__ == '__main__':
    main()
