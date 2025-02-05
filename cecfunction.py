# -*- coding: utf-8 -*-
"""CECFunction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TVhsY2zuF9arVYgbuL9MJZoBIJ3d7UWQ

#F1
"""
import numpy

def F1(x):
    s = numpy.sum(x ** 2)
    return s

"""#F3"""

def F3(x):
    dim = len(x) + 1
    o = 0
    for i in range(1, dim):
        o = o + (numpy.sum(x[0:i])) ** 2
    return o

"""#F5"""

def F5(x):
    dim = len(x)
    o = numpy.sum(
        100 * (x[1:dim] - (x[0 : dim - 1] ** 2)) ** 2 + (x[0 : dim - 1] - 1) ** 2
    )
    return o

"""#F6"""

def F6(x):
    o = numpy.sum(abs((x + 0.5)) ** 2)
    return o

"""#F8"""

def F8(x):
    o = numpy.sum(-x * (numpy.sin(numpy.sqrt(numpy.abs(x)))))
    return o