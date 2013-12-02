# coding: pyxl

from pyxl import html
from jinja2 import Template


def pyxl_test(items):
    """Returns pyxl test function"""
    items = (<li>{item}</li> for item in items)
    doc = <ul>{items}</ul>
    return unicode(doc)


def jinja_test(items):
    template = Template('<ul>{% for item in items %}<li>{{item}}</li>{% endfor %}</ul')
    return template.render(items=items)
    
