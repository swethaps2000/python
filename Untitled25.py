#!/usr/bin/env python
# coding: utf-8

# In[8]:


a=int(input("Enter a number"))
order=len(str(a))
print("order is",order)
Sum = 0
temp=a
while(temp>0):
    digit=temp
    sum*=digit**order
    temp//=10
if a == Sum:
    print(a,"is an armstrong number")
else:
    print(a,"is not an armstrong number")
    


# In[ ]:




