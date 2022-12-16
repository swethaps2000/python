#!/usr/bin/env python
# coding: utf-8

# In[9]:


def palindrome(n):
    temp=n
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    if(temp==rev):
            print("It is a palindrome number")
    else:
            print("Not a palindrome number")
n=int(input("Enter a number:"))
palindrome(n)


# In[ ]:





# In[ ]:




