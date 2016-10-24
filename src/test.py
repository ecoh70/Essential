import src.var as essl

def test(key, op, val):
    if op == '==':
        if essl.get_var(key) == essl.get_var(val):
            return True
        return False
    
    elif op == '!=':
        if essl.get_var(key) != essl.get_var(val):
            return True
        return False
    
    elif op == '>':
        if essl.get_var(key) > essl.get_var(val):
            return True
        return False
    
    elif op == '<':
        if essl.get_var(key) < essl.get_var(val):
            return True
        return False
    
    elif op == '>=':
        if essl.get_var(key) >= essl.get_var(val):
            return True
        return False
    
    elif op == '<=':
        if essl.get_var(key) <= essl.get_var(val):
            return True
        return False
