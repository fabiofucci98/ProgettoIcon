def greater(a, b):
    return eval(a.const+'>'+b.const)


def equals(a, b):
    if a.const == b.const:
        return True
    return eval(a.const+'=='+b.const)


built_ins = {'greater': greater, 'equals': equals}
