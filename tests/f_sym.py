import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import engine as e


en = e.Engine()
en.load_kb('f_sym')
q = e.parse('greater(succ(9),9).')
ans = en.prove(q)


for c in en.kb:
    print(c)


print(ans)
