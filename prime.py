#!/usr/bin/env python
# coding: utf-8

# In[15]:


num=int(input("Enter a number"))
if num>1:
    for i in range(2,num):
         if(num%i==0):
            print(num,"is not prime number")
            break;
    else:
            print(num,"is a prime number")

else:
    print(num,"is not a prime number")


# In[ ]:





# In[ ]:




