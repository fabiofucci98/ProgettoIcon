import Engine as e

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


# Primo esempio con un albero di derivazione più profondo
query = 'a,d'
query = engine.parse_query(query)
print(clean(engine.prove(query))
      )
# Esempio con individui e regole
query = 'rotto(X)'
query = engine.parse_query(query)
print(clean(engine.prove(query))
      )

# Semplice derivazione con individui
query = 'imm_west(X,Y)'

query = engine.parse_query(query)
print(clean(engine.prove(query))
      )

# Derivazioni con naf
query = 'a1'
query = engine.parse_query(query)
print(clean(engine.prove(query))
      )


query = 'not_a1'
query = engine.parse_query(query)
print(clean(engine.prove(query))
      )

# Derivazione con naf e predicati
query = 'p(X)'
query = engine.parse_query(query)
print(clean(engine.prove(query))
      )

# Cicli
query = 'a2'
query = engine.parse_query(query)
print(clean(engine.prove(query))
      )
query = engine.parse_query(input())
while(True):
    if query:
        print(clean(engine.prove(query))
              )
    else:
        print('syntax error')
    query = engine.parse_query(input())
