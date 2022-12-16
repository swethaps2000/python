#!/usr/bin/env python
# coding: utf-8

# In[14]:


print("ENTER THE INTERVAL TO FIND THE PRIME NUMBERS IN BETWEEN")
a=int(input("Enter the first interval "))
b=int(input("Enter the second interval "))
for i in range(a,b+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
       


# In[ ]:





# In[ ]:




