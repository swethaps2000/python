#!/usr/bin/env python
# coding: utf-8

# In[9]:


def power(e,x):
    if x==0:
        return 1
    else:
        return e*power(e,x-1)
e=int(input("ENTER THE BASE : "))
x=int(input("ENTER THE POWER : "))
print(e,"^",x,"=",power(e,x))
    


# In[ ]:




