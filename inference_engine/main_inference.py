import Engine as e

engine = e.Engine()
engine.load_kb()


query = 'rotto(braccio), culo'
query = engine.parse_query(query)
print(engine.ask(query)
      )
query = 'imm_west(X,Y)'

query = engine.parse_query(query)
print(engine.ask(query)
      )


pred = engine.parse_query(input())
while(True):
    if pred:
        print(engine.ask(pred))

    else:
        print('syntax error')
    pred = engine.parse_query(input())
