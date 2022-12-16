#!/usr/bin/env python
# coding: utf-8

# In[3]:


def fib(n):
    if n<=1:
        return n
    else:
        return(fib(n-1)+fib(n-2))
x=int(input("enter the numbe of terms"))
if (x<=0):
    print("enter a positive number")
else:
    print("finonacci series")
    for i in range(x):
        print(fib(i))

    


# In[ ]:




