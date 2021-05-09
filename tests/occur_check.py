import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import engine as e

en = e.Engine()

en.load_kb('occur_check')
q = e.parse('lt(Y,Y).')
ans = en.prove(q)
print(ans)

ans = en.prove(q,occurs_check=False)

print(ans)
