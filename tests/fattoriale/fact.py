import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.append(parentdir)

import engine as e
from built_in import built_in_preds,built_in_funcs
en = e.Engine(built_in_funcs,built_in_preds)
"Calcola il fattoriale"
en.load_kb('fact')
n = 1
print('premere invio per valutare il fattoriale del numero successivo\n')
while True:
    print('fattoriale di: '+str(n))
    query = e.parse('factorial('+str(n)+',1,F).')
    print('query: '+str(query))
    a = en.prove(query,prove_one=True)
    
    print(a[-1][-1])
    n+=1
    input()