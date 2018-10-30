def answer(s):    
    right=0
    salutes=0
    for l in s:
        if(l=='>'):
            right+=1
        if(l=='<' and right>0):
            salutes += 2 * right        
    return salutes

print(answer("<<>><"))