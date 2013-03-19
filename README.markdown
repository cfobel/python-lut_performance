<!--Copyright 2013 - Christian Fobel <christian (a inside of a circle) dot net> -->


# Purpose

The idea is to answer the following question:

    Is it faster to create and store a lookup table to translate a tuple
    to a one-dimensional flattened index, or is it faster to calculate
    the flattened index?

To test this, we create a lookup table (i.e., dictionary) mapping each
permutation of 34x34 to a one-dimensional index value, calculated as:

    tuple[0] * 34 + tuple[1]

To push the experiment further, a Cython version is also included for
comparison.


# Methodology

Run test where a lookup table is created once, after which several trials are
run, where each trial performs a specific number of accesses.  For all of the
trials conducted, a lookup table of size `34 * 34 = 1156` is used.  The results
show the time required to create the lookup table, along with the runtime to
retrieve 10,000 items in pure Python by a) looking up the item using a
two-tuple key, or b) by calculating the result from scratch.  In addition, the
results show the runtimes for accessing 10,000-160,000 items using Cython
implementations.


# Results

While not the originally intended focus of this experiment, a point of
particular interest is the significant performance increase by using minimally
modified version of the pure Python code by compiling the code using Cython.
The lookup-table and the calculation Cython implementations both exhibited a 2x
run-time speedup over the pure Python implementations.

In regards to the look-up table access performance vs\. calculating the items
from scratch, while the item access time is lower (significantly so, in the
pure Python implementations) for the look-up table runtimes compared to
calculating the item from scratch, it takes many accesses to make up for the
creation time of the lookup table.  However, it looks like the overhead of the
look-up table creation becomes insignificant when performing more than 200,000
accesses.

Note that all of the results shown and discussed here are only for one test
system (as described below) and should not be taken as anything more than my
mere musings.


Results:

    Runtime to create lookup table: 1.87200903893

    Python runtimes: lut: 1.214227 seconds, calc: 2.186246 seconds

    Cython runtimes:
        [n= 10000] lut: 0.623161971569 seconds, calc: 0.716995000839 seconds
        [n= 20000] lut: 1.2475579977 seconds, calc: 1.43316102028 seconds
        [n= 40000] lut: 2.49550104141 seconds, calc: 2.8736000061 seconds
        [n= 80000] lut: 5.00199699402 seconds, calc: 5.72012519836 seconds
        [n=160000] lut: 10.0692577362 seconds, calc: 11.5044851303 seconds

Test system:

      Model Name: Intel(R) Core(TM) i7-3517U CPU @ 1.90GHz
         Cpu Mhz: 1900.000
      Cache Size: 4096 KB
        Bogomips: 4789.15
