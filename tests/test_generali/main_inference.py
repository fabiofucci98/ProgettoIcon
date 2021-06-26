import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)

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


# Esempio con naf su individui
query = 'not_pp(d).'
print('query: ' + query)
query = 'not_pp(d).'
query = e.parse(query)
print(clean(engine.prove(query))
      )
print(engine.how(query[0]))
print()
# Primo esempio con un albero di derivazione più profondo
query = 'a,d.'
print('query: ' + query)
query = e.parse(query)
print(clean(engine.prove(query))
      )
print(engine.how(query[0]))
print(engine.how(query[1]))
print()
# Esempio con individui e regole
query = 'rotto(X).'
print('query: ' + query)
query = e.parse(query)
print(clean(engine.prove(query))
      )
print(engine.how(query[0]))
print()

# Semplice derivazione con individui
query = 'imm_west(X,Y).'

print('query: ' + query)
query = e.parse(query)
print(clean(engine.prove(query))
      )
print(engine.how(query[0]))
print()

# Derivazioni con naf
query = 'a1.'
print('query: ' + query)
query = e.parse(query)
print(clean(engine.prove(query))
      )
print(engine.how(query[0]))
print()


query = 'not_a1.'
print('query: ' + query)
query = e.parse(query)
print(clean(engine.prove(query))
      )
print(engine.how(query[0]))

print()
# Derivazione con naf e predicati
query = 'p(X).'
print('query: ' + query)
query = e.parse(query)
print(clean(engine.prove(query))
      )
print(engine.how(query[0]))

print()
# Cicli
query = 'a2.'
print('query: ' + query)
query = e.parse(query)
print(clean(engine.prove(query))
      )
print(engine.how(query[0]))
