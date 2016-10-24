import parse_expr import parse_expr

variables = {}
global variables

functions = {}
global functions

def getVar(key):
    if key[0] == '%':
        if key[1:] not in variables:
            return None
        return variables[key[1:]]
    elif key[-1] in ('+', '-', '/', '*'):
        return parse_expr(key)
    else:
        return key

def set_var(key, val):
    variables[key] = get_var(val)
    return get_var(key)
