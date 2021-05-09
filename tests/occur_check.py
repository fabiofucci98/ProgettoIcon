import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import engine as e
from engine import Constant, Variable

def occur_check(X, const):
    if isinstance(const, Variable):
        return X == const
    elif len(const.args) == 0:
        return False
    else:
        for arg in const.args:
            if occur_check(X, arg):
                return True
        return False

c = Constant('c',[Constant('c',[Variable('X')])])
v = Variable('X')
print(occur_check(v,c))

en = e.Engine()


en.load_kb('occur_check')
q = e.parse('lt(Y,Y).')
ans = en.prove(q)
print(ans)
