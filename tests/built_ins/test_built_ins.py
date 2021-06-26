import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)

sys.path.append(parentdir)
import engine as e
"Test per verificare la possibilità di aggiungere propri predicati e funzioni"
def fact(n):
    prod = 1
    for i in range(1, int(n.const)+1):
        prod *= i
    return e.Constant(str(prod))


def is_two_n_plus_one(n1, n2):
    return eval('2*'+n1.const+'+1=='+n2.const)


en = e.Engine()
en.built_in_funcs['fact'] = fact
en.built_in_preds['is_two_n_plus_one'] = is_two_n_plus_one

q = e.parse('is_two_n_plus_one(fact(5),241).')

print(en.prove(q))
