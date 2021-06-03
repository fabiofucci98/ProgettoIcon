import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import engine as e


en = e.Engine()
en.load_kb('f_sym')


f = e.parse('p(sum(succ(succ(succ(9))),3)).')
ans = en.prove(f)
print(ans)
f = e.parse('p(mul(succ(succ(succ(9))),3)).')
ans = en.prove(f)
print(ans)
f = e.parse('p(div(succ(succ(succ(9))),3)).')
ans = en.prove(f)
print(ans)
f = e.parse('p(sub(succ(succ(succ(9))),3)).')
ans = en.prove(f)
print(ans)
f = e.parse('greater(sum(succ(succ(succ(9))),3),14).')
ans = en.prove(f)
print(ans)
f = e.parse('greater_equal(sum(succ(succ(succ(9))),3),sum(succ(succ(succ(9))),3)).')
ans = en.prove(f)
print(ans)
f = e.parse('p(f(x)).')
ans = en.prove(f)
print(ans)
