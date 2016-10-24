import src.exec as essl
import src.var

def call(method, args):
    stack = []
    for arg in args:
        stack.append(var.get_var(args))
        
    return essl.exec(var.functions[method], stack)
