import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import engine as e


def p(kb, ass):
    print('kb')

    for clause in kb:
        print(clause)

    print('ass')
    for as_ in ass:
        print(as_)


en = e.Engine()
en.load_kb('test_false_ind')
q = e.parse('false.')
ans = en.prove(q, abduce=True)
print([elem[-1] for elem in ans])
