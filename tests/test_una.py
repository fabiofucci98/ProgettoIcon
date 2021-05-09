import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import engine as e

en = e.Engine()
en.load_kb('test_una')

q = e.parse('passed_two_courses(sam).')
ans = en.prove(q)
print(ans)