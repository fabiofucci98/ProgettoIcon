#Predicati

def less(a, b):
    return eval(a.const+'<'+b.const)


def greater(a, b):
    return eval(a.const+'>'+b.const)


def greater_equal(a, b):
    return eval(a.const+'>='+b.const)


def equals(a, b):
    if a.const == b.const:
        return True
    return eval(a.const+'=='+b.const)

#Funzioni

def succ(n):
    return eval(n.const+'+1')


def sum(a, b):
    return eval(a.const+'+'+b.const)


def mul(a, b):
    return eval(a.const+'*'+b.const)


def div(a, b):
    return eval(a.const+'//'+b.const)


def sub(a, b):
    return eval(a.const+'-'+b.const)


built_in_funcs = {'succ': succ, 'sum': sum,
                  'mul': mul, 'div': div, 'sub': sub}


built_in_preds = {'greater': greater,
                  'equals': equals, 'greater_equal': greater_equal}
