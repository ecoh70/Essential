import parse_expr import parse_expr

class var_hand(object):
    def __init__(self):
        variables = {}

    def getVar(self, key):
        if key[0] == '%':
            if key[1:] not in self.variables:
                return None
            return self.variables[key[1:]]
        elif key[-1] in ('+', '-', '/', '*'):
            return parse_expr(key)
        else:
            return key

    def set_var(self, key, val):
        self.variables[key] = get_var(val)
        return get_var(key)
