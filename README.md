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


Updating requirements.txt
-------------------------

If you wish to introduce new dependency, then please, add it
to `requirements.in` file and then run `pip-compile` command.

Pylinting your templates
------------------------

Some people are wondering if tools like pylint will treat files
with embedded html as full of syntax errors. I tested the `test.py`
with pylint and must admit, there is no problems unless you installed
pyxl system-wide or run `pylint` like this, to register proper codec
before pylint started:

    python -c "import pyxl.codec.register, sys; \
              from pkg_resources import load_entry_point; \
              sys.exit(load_entry_point('pylint', 'console_scripts', 'pylint')())" \
           test.py