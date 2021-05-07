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
en.load_kb('test_false')
q = e.parse('false.')
ans = en.prove(q, abduce=True)
print(ans[0][-1], ans[1][-1])

en.load_kb('test_abduce')
q = e.parse('wheezing.')
ans = en.prove(q, abduce=True)
print(ans[0][-1], ans[1][-1])
