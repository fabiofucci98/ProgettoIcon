import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)

sys.path.append(parentdir)
import engine as e

en = e.Engine()
"Test per verificare il funzionamento del controllo di occorrenza"
en.load_kb('occur_check')
q = e.parse('lt(Y,Y).')
print('valutazione di lt(Y,Y) con controllo di occorrenza:')
ans = en.prove(q)
print(ans)
print('valutazione di lt(Y,Y) senza controllo di occorrenza')
ans = en.prove(q,occurs_check=False)
print(ans)
