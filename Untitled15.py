#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cmath
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))
d=complex(b**2)-(4*a*c)
x1=(-b+cmath.sqrt(d))/ (2*a)
x2=(-b-cmath.sqrt(d))/ (2*a)
print("The solution for the euations are",x1,x2)


# In[ ]:




