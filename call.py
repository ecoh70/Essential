from essl import exec
from essl import vars

def call(method, args):
    stack = []
    for arg in args:
        stack.append(vars.get_var(args))
    return essl.exec(vars.functions[method], stack)
