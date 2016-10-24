import src.classes as essl

def parse(src):
    stack = [[]]
    word, prev_sym = '', ''
    in_str, in_quote = False, False
    for sym in src:
        
        # blocks:
        if word in ('method', 'if', 'for') and not in_str and not in_quote:
            stack.append([])
            stack[-1].append(word)
            word = ''
            
        elif word == 'end' and not in_str and not in_quote:
            if stack:
                stack[-1].append(word)
                word = ''
            stack.append([])
            
        # multi-char operators:
        elif word in ('==', '!=', '>', '<', '>=', '<='):
            stack[-1].append(word)
            word = ''
            
        # symbols:
        elif sym == '(' and not in_str and not in_quote:
            stack.append([])
            if word:
                stack[-1].append(word)
                word = ''
                
        elif sym in (';', '\n') and not in_str and not in_quote:
            if stack:
                stack[-1].append(word)
                word = ''
            stack.append([])
            
        elif sym == '[':
            stack.append([])
            if word:
                stack[-1].append(word)
                word = ''
                
        elif sym in ')' and not in_str and not in_quote:
            if word:
                stack[-1].append(word)
                word = ''
            temp = stack.pop()
            stack[-1].append(temp)
            args_t = stack[-1]
            stack.remove(args_t)
            stack[-1].append(essl.Args(args_t))
            
        elif sym == ']' and not in_str and not in_quote:
            if word:
                stack[-1].append(word)
                word = ''
            temp = stack.pop()
            stack[-1].append(temp)
            list_t = stack[-1]
            stack.remove(list_t)
            stack[-1].append(essl.List(list_t))
            
        elif sym in (' ', '\t') and not in_str and not in_quote:
            if word:
                stack[-1].append(word)
                word = ''
                
        elif sym == '\"' and not prev_sym == '\\':
            in_str = not in_str
            if in_str:
                str_t = stack[-1]
                stack.remove(str_t)
                stack[-1].append(essl.String(str_t))
                
        elif sym == '\'' and not prev_sym == '\\':
            in_quote = not in_quote
            if in_quote:
                quote_t = stack[-1]
                stack.remove(quote_t)
                stack[-1].append(essl.Quote(quote_t))
                
        elif sym in ('=', '!', '>', '<', '+', '-', '*', '/'):
            if word:
                stack[-1].append(word)
                word = ''
            word += sym
            
        else:
            word += sym
            prev_sym = sym
            
    if word:
        stack[-1].append(word)
        word = ''

return stack[0]
