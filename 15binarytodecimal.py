#!/usr/bin/env python
# coding: utf-8

# In[77]:


def btod(a):
    i=len(str(a))
    x=a%10
    print("length is",i)
    sum=0
    for j in range(0,i):
                x=a%10
                sum+=x*(2**j)
                a//=10
    print("The decimal value is ",sum)

x=int(input("Enter a BINARY NUMBER for converting to DECIMAL "))
z=btod(x)


# In[ ]:





# In[ ]:





# In[ ]:




