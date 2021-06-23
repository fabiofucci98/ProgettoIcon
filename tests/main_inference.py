import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import engine as e

engine = e.Engine()
engine.load_kb('kb')


def clean(SLD_derivations):
    if not isinstance(SLD_derivations, list):
        return True

    tmp_answers = [der[-1].head.args for der in SLD_derivations]
    answers = []
    for answer in tmp_answers:
        if answer not in answers:
            answers.append(answer)

    if len(answers) == 0:
        return False

    elif len(answers) == 1 and len(answers[0]) == 0:
        return True

    return answers

query = 'not_pp(d).'
query = e.parse(query)
print(clean(engine.prove(query))
      )
print(engine.how(query[0]))
# Primo esempio con un albero di derivazione più profondo
query = 'a,d.'
query = e.parse(query)
print(clean(engine.prove(query))
      )
print(engine.how(query[0]))
print(engine.how(query[1]))
# Esempio con individui e regole
query = 'rotto(X).'
query = e.parse(query)
print(clean(engine.prove(query))
      )
print(engine.how(query[0]))

# Semplice derivazione con individui
query = 'imm_west(X,Y).'

query = e.parse(query)
print(clean(engine.prove(query))
      )
print(engine.how(query[0]))

# Derivazioni con naf
query = 'a1.'
query = e.parse(query)
print(clean(engine.prove(query))
      )
print(engine.how(query[0]))


query = 'not_a1.'
query = e.parse(query)
print(clean(engine.prove(query))
      )
print(engine.how(query[0]))

# Derivazione con naf e predicati
query = 'p(X).'
query = e.parse(query)
print(clean(engine.prove(query))
      )
print(engine.how(query[0]))

# Cicli
query = 'a2.'
query = e.parse(query)
print(clean(engine.prove(query))
      )
print(engine.how(query[0]))

query = e.parse(input())
while(True):
    print(engine)
    if query:
        print(clean(engine.prove(query))
              )
        print(engine.how(query))

    else:
        print('syntax error')
    query = e.parse(input())
