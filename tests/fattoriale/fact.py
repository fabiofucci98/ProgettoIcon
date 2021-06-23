import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.append(parentdir)

import engine as e

en = e.Engine()
"Calcola il fattoriale"
en.load_kb('fact')
n = 1
while True:
    query = e.parse('factorial('+str(n)+',1,F).')
    print('query: '+str(query))
    a = en.prove(query,prove_one=True)
    
    print(a[-1][-1])
    input()
    n+=1