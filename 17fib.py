#!/usr/bin/env python
# coding: utf-8

# In[8]:


def fibonacci(n):
    n1,n2=0,1
    sum=0
    if n==1:
        print(n1)
    else:
        print("fibonacci series:")
        while(sum<n):
            print(n1)
            y=n1+n2
            n1=n2
            n2=y
            sum+=1
n=int(input("enter the range"))
fibonacci(n)


# In[ ]:





# In[ ]:




