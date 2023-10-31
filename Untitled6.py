#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# temprature is in degree
c=float(input("enter temprature"))
# convertion of c in f
f=(9/5)*c+32
print("in f",f)


# In[ ]:


# wap to convert sec into hours min and sec
time=int(input("enter time into sec"))
h=time//3600
m=(time//60)-(h*60)
s=time-(h*3600)-(m*60)
print(h, "hour",m, "time",s, "sec")


# In[ ]:


# wap to convert sec into hours min and sec
time=int(input("enter time into sec"))
h=time//3600
m=(time//60)-(h*60)
s=time-(h*3600)-(m*60)
print(h, "hour",m, "time",s, "sec")


# In[ ]:


x=10
if x>5:
    print("positive")
else:
    print("neg")


# In[ ]:


# wap to check given input numbr is even or odd
num=int(input("enter number : "))
if num%2==0:
    print("number is even")
else:
    print("numer is odd")


# In[ ]:


# wap to get 3 num and give lare num
a=int(input("enter first num : "))
b=int(input("enter second num : "))
c=int(input("enter third num : "))
if a>b:
    if a>c:
        print("a is max")
    else :
        print("c is max")
elif b>c:
    print("b is max")
else:
    print("c is max")


# In[ ]:


# wap to check if number is div by 7 and 6
num=int(input("enter number : "))
if num%6==0:
    if num%7==0:
        print("number not is div by 6 & 7")
    else:
        print("not div by 6 & 7")
else:
    print("not div by 6")


# In[3]:


year=int(input("enter leap year : "))
if year%4==0:
    if year%100==0 :
        if year%400==0 :
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")     


# In[ ]:




