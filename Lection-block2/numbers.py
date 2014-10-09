__author__ = 'Djonny'
import math

class Numbers:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        if c > 0:
            self.c = c
        else:
            self.c = 0
    def sum(self):
        return self.a + self.b + self.c
    def mult(self):
        return self.a * self.b * self.c
    def abs_mult(self):
        return math.fabs(self.a * self.b * self.c)

num=Numbers(1,2,-3)
print num.sum()
print num.mult()
print num.abs_mult()
