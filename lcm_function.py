# -*- coding: utf-8 -*-
"""LCM Function.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VniA0gAUIFMs1HdTTLPwgq5MrZ0KsJA0
"""

import math

def lcm(a, b):

    return abs(a * b) // math.gcd(a, b)

print(lcm(2, 7))
print(lcm(121, 17))
print(lcm(72, 13))