#!/usr/bin/env python
# coding: utf-8

# In[18]:


def fact(x):
    if x==1:
        return x
    else:
        return x*fact(x-1)
x=int(input("ENTER A NUMBER: "))
if x<0:
    print("factorial doesn't exist")
elif x==0:
    print("factorial of 0 is 1")
else:
    print("factorial of ",x,"is",fact(x))


# In[ ]:





# In[ ]:





# In[ ]:




