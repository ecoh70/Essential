from src import var

def test(key, op, val):
    if op == '==':
        if var.get_var(key) == var.get_var(val):
            return True
        return False
    
    elif op == '!=':
        if var.get_var(key) != var.get_var(val):
            return True
        return False
    
    elif op == '>':
        if var.get_var(key) > var.get_var(val):
            return True
        return False
    
    elif op == '<':
        if var.get_var(key) < var.get_var(val):
            return True
        return False
    
    elif op == '>=':
        if var.get_var(key) >= var.get_var(val):
            return True
        return False
    
    elif op == '<=':
        if var.get_var(key) <= var.get_var(val):
            return True
        return False
