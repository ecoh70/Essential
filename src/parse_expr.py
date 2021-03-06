import src.var as essl

def parse_expr(expr):
    stack = []
    for term in expr:
        if not term in ('+', '-', '*', '/'):
            stack.append(essl.get_var(term))
            
        elif term in ('+', '-', '/', '*'):
            operand = stack.pop()
            operand2 = stack.pop()
            if term == '+':
                stack.append(operand1 + operand2)
                
            elif term == '-':
                stack.append(operand1 - operand2)
                
            elif term == '*':
                stack.append(operand1 * operand2)
                
            elif term == '/':
                stack.append(operand1 / operand2)
                
    return stack[0]
