# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.
from somelibrary.module import somefunc


class SimpleBenchmark(object):
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        pass
    
    def time_somfunc(self):
        somefunc()

