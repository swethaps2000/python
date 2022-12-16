#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Enter the measure of sides of the triangle")
a=int(input())
b=int(input())
c=int(input())
s=(a+b+c)/2
area=s*(s-a)*(s-b)*(s-c)**0.5
print("Area of the triangle is",area)


# In[ ]:




