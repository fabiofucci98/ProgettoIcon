import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)

sys.path.append(parentdir)
import engine as e

"""
Test su due basi di conoscenza fornite da esempi del libro per verificare il funzionamento
del ragionamento abduttivo e diagnosi basata su consistenza
"""
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
print([elem[-1] for elem in ans])

en.load_kb('test_abduce')
q = e.parse('wheezing.')
ans = en.prove(q, abduce=True)
print([elem[-1] for elem in ans])
