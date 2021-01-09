#!/usr/bin/env python
# coding: utf-8

# In[27]:


from numdigit import numdigit
from test import test

def multiply(a,b):
    if (a == 0)|(b==0):
        return 0
    elif ((a>0) & (b>0)) | ((a<0) & (b<0)):
        sign = True
    else:
        sign = False
        
    a = abs(a)
    b = abs(b)
    da=numdigit(a)
    db=numdigit(b)
    
    if (da == 1)|(db==1):
        result = a*b
        if sign == False:
            result *= -1
        return result
    
    if da > db:
        n = da//2
    else:
        n = db//2
    a1,a2 = divmod(a,10**n)
    b1,b2 = divmod(b,10**n)
    a1b1 = multiply(a1,b1)
    a2b2 = multiply(a2,b2)
    a1b2plusa2b1=multiply(a1+a2,b1+b2) - a1b1 - a2b2
    result = (10**(2*n))*a1b1 + (10**n)*a1b2plusa2b1 + a2b2
    if (sign==False):
        result *= -1
    return result   


# In[28]:


test(multiply(12,0),0)
test(multiply(0,100),0)
test(multiply(12,23),276)
test(multiply(1234,2345),2893730)
test(multiply(2,6),12)
test(multiply(12567,23),289041)
test(multiply(12567,-1),-12567)

