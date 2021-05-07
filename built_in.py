def greater(a, b):
    return eval(a.const+'>'+b.const)


def equals(a, b):
    if a.const == b.const:
        return True
    return eval(a.const+'=='+b.const)


"""
def solve_funcs(gac):
    for i in range(len(gac.head.args)):
        gac.head.args[i]=rec_solve(gac.head.args)

    for i in range(len(gac.body))
    gac.head.args = rec_solve(gac.head.args)
    gac.body = [rec_solve(atom.args) for atom in gac.body]
    return gac
"""


def rec_solve(const):
    return const


built_in_preds = {'greater': greater, 'equals': equals}
built_in_funcs = {}
