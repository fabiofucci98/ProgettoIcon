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
    for a in en.prove(query):
        print(a[-1])
    n+=1