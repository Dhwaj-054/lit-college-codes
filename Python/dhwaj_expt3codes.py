#!/usr/bin/env python
# coding: utf-8

# In[27]:


#expt 3A
lim= int(input("enter limit of sequence:"))
x=1
print(x)
for i in range (0, lim-1):
    x=x*2
    print(x)


# In[4]:


#expt3 B
num = int(input("enter a number to check:"))
cp=num
rev=0
while num>0:
    rev=(rev*10)+(num%10)
    num //= 10

if cp==rev:
    print("it is a palindrome no")
else:
    print("it isnt palindrome")


# In[14]:


#expt 3C
start=int(input("enter start of range: "))
end=int(input("enter end of range: "))
print("prime no is given range: ")
for i in range (start, end +1):
    count=0
    for j in range (1, i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)


# In[6]:


#expt 3D
num = int(input("enter a number to count its digits: "))
cp=num
dig=0
while num>0:
    dig+=1
    num //= 10
if cp==0:
    dig=1
    
print("total no of digits in the number are:", dig)


# In[72]:


#expt 3 E
for i in range(0,5):
    for j in range(0,9):
        if (i==0 or i==4):
            if (j==1 or j==2 or j==3 or j==5 or j==6 or j==7):
                print(" ", end= " ")
            else:
                print("*", end= " ")
        elif (i==1 or i==3):
            if (j==1  or j==2 or j==4 or j==6 or j==7):
                print(" ",end=" ")
            else:
                print("*",end =" ")
        elif(i==2):
            if (j==1 or j==3 or j==5 or j==7):
                print(" ", end= " ")
            else:
                print("*",end=" ")
    print()


# In[71]:


#expt 3 E
sp=" "
for i in range(1,6):
    for j in range(3,i+1):
        if (j%2==0) :
            print("*",sp,sp,sp,"*",sp,sp,sp,"*")
            
        elif(j%3==0):
             print("*",sp,sp,"*",sp,"*",sp,sp,"*")
                
        elif (j%5==0):
            print("*",sp,"*",sp,"*",sp,"*",sp,"*")
    


# In[ ]:





# In[ ]:




