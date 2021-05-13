import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import engine as e

en = e.Engine()

en.load_kb('coloring')
queries = []
f = open('coloring_queries', 'r')
for line in f:
    if line[-1] == '\n':
        line = line[0:-1]
    queries.append(e.parse(line))
for query in queries:
    ans = en.prove(query)
    print('query: '+str(query))
    if len(ans) == 0:
        print(None)
    for a in ans:
        print(a[-1])
    print()
