#!/usr/bin/env python
# coding: utf-8

# In[3]:


try:
    fileptr=open("abc.txt","r")
    try:
        fileptr.write("Hi Im good")
    finally:
        fileptr.close()
        print("File closed")
except:
        print("Error")


# In[ ]:




