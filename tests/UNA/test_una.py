import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)

sys.path.append(parentdir)
import engine as e
"Test per verificare che la CWA include l'UNA"
en = e.Engine()
en.load_kb('test_una')

q = e.parse('passed_two_courses(sam).')
ans = en.prove(q)


for a in ans:
    for b in a:
        print(b)
