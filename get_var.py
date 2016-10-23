import parse_expr

variables = {}

def getVar(key):
    if key[0] == '%':
        return variables[key[1:]]
    elif key[-1] in ('+', '-', '/', '*'):
        return parse_expr(key)
    else:
        return key
