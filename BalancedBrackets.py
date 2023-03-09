def isBalanced(x):
    stack = []
    
    for i in x:
        if i in '({[':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            
            ch = stack.pop()
            
            if ch == '(':
                if i != ')':
                    return False
        
            elif ch == '{':
                if i != '}':
                    return False
            
            elif ch == '[':
                if i != ']':
                    return False
    
    if stack:
        return False
    
    return True
