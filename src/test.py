from vars import get_var

def test(var, op, val):
    if op == '==':
        if get_var(var) == get_var(val):
            return True
        return False
    
    elif op == '!=':
        if get_var(var) != get_var(val):
            return True
        return False
    
    elif op == '>':
        if get_var(var) > get_var(val):
            return True
        return False
    
    elif op == '<':
        if get_var(var) < get_var(val):
            return True
        return False
    
    elif op == '>=':
        if get_var(var) >= get_var(val):
            return True
        return False
    
    elif op == '<=':
        if get_var(var) <= get_var(val):
            return True
        return False
