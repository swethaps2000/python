#!/usr/bin/env python
# coding: utf-8

# In[4]:


a=int(input("ENTER NUMEBR 1:"))
b=int(input("ENTER NUMEBR 2:"))
print("menu\n1-Addition\n2-Substraction\n3-multiplication\n4-division")
choice=int(input("Enter your choice:"))

if(choice==1):
    c=a+b
    print("Sum=:",c)

elif(choice==2):
    c=a-b
    print("Substraction is=:",c)
elif(choice==3):
    c=a*b
    print("Multiplication is=:",c)
elif(choice==4):
    c=a/b
    print("Division is=:",c)
else:
        print("INVALID CHOICE!")
    


# ### 
