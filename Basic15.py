# Write a Python program to check the priority of the four operators(+,-,*,/)
from collections import deque
import re

_operators_ = "+-/*"
_parenthesis_ = "()"
_priority_ = {
    '+' : 0,
    '-' : 0,
    '*' : 1,
    '/' : 1,
}

def test_higher_priority(operator1,operator2):
    return _priority_[operator1] >= _priority_[operator2]

print(test_higher_priority('*','-'))
print(test_higher_priority('+','-'))
print(test_higher_priority('+','*'))
print(test_higher_priority('+','/'))
print(test_higher_priority('*','/'))