A simple comparison test of pyxl and jinja2
===========================================

On my macbook air `pyxl` is faster than `jinja2` by 26%:

    $ ipython
    
    In [1]: import pyxl.codec.register
    
    In [2]: import test
    
    In [3]: items = range(100)
    
    In [4]: %timeit test.pyxl_test(items)
    1000 loops, best of 3: 773 µs per loop
    
    In [5]: %timeit test.jinja_test(items)
    1000 loops, best of 3: 1.05 ms per loop


Feel free to improve these tests and to add another templating
engines.