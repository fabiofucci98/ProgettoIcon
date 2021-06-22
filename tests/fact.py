import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import engine as e

en = e.Engine()

en.load_kb('fact')
n = 1
while True:
    query = e.parse('factorial('+str(n)+',1,F).')
    print('query: '+str(query))
    a = en.prove(query,prove_one=True)
    
    print(a)
    input()
    n+=1