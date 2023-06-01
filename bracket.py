open=["(","{","["]
close=[")","}","]"]

def balance(expr):
    stack=[]
    for i in open:
        if i in open:
            stack.append[i]
        elif i in close:
            p=close.index(i)
            if((len(stack)>0)):
                open(p)==stack[len(stack)-1]
                stack.pop()
            else:
                return "unbalanced"
    if len(stack)==0:
            return "balanced"
    else:
            return "unbalanced"
            


expr=input("enter the value")
print("the given expression is %s"%(balance(expr)))
            
