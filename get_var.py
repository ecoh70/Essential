import parse_expr

def getVar(variables, key):
    if key[0] == '%':
        if key[1:] not in variables:
            return None
        return variables[key[1:]]
    elif key[-1] in ('+', '-', '/', '*'):
        return parse_expr(key)
    else:
        return key

def set_var(variables, key, val):
    variables[key] = get_var(val)
    return get_var(variables, key)
