#!/usr/bin/env python
# coding: utf-8

# In[29]:


def count(list,n):
    count=0
    for i in list:
        for k in i:
            if k==n:
                count=count+1
    return count
li=[]
n=int(input("enter the size of list: "))
for i in range (0,n):
        e=input("enter the elemts of list: ")
        li.append(e)
        print(li)
x=input("enter the character to found :")
print(count(li,x))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




