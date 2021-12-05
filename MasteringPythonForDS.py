#!/usr/bin/env python
# coding: utf-8

# # This is Python for Data Science Tutorial

# This is an Introductory Course to Data Science using Python

# In[2]:


print ("Hello World")


# #  Variables

# In[9]:


x = 3


# In[10]:


get_ipython().run_line_magic('whos', '')


# In[11]:


print(type(x))


# In[12]:


x = 5.7


# In[13]:


get_ipython().run_line_magic('whos', '')


# In[14]:


print(type(x))


# In[15]:


abcd = 5567.32


# In[16]:


get_ipython().run_line_magic('whos', '')


# In[17]:


a,b,c,d,e = 3,4,5.6,7.2, -3


# In[18]:


get_ipython().run_line_magic('whos', '')


# In[19]:


del abcd


# In[20]:


print(abcd)


# In[22]:


c = 2+5j


# In[23]:


print(type(c))


# In[25]:


s = 'This is Cyber Crafts Academy'


# In[26]:


print(type(s))


# # Operators

# In[28]:


get_ipython().run_line_magic('whos', '')


# In[29]:


sumOfaAndb = a+b


# In[30]:


print(sumOfaAndb)


# In[31]:


print(type(sumOfaAndb))


# In[32]:


type(a+d)


# In[33]:


v = ((a+d)**3)/4


# In[34]:


print(v)


# In[35]:


type(v)


# In[36]:


s1 = "Hello"
s2 = "World"


# In[37]:


print(s1+s2)


# In[38]:


10/3


# In[39]:


10//3


# In[40]:


_


# Exercise

# Can a variable name start with a digit?
# Is 5y a variabel name?

# In[47]:


5y = 5


# In[48]:


@v = 4


# In[49]:


*h = 4


# In[50]:


_k = 6


# In[45]:


startingTimeOfTheCourse = 2.0


# In[51]:


get_ipython().run_line_magic('whos', '')


# # Boolean

# In[55]:


a = True
b = True
c = False


# In[56]:


get_ipython().run_line_magic('whos', '')


# In[57]:


print(a and b)
print(a and c)
print(c and a)


# In[59]:


d = a or c
print(d)


# In[60]:


not(a)


# In[61]:


not(b)


# In[62]:


not(c)


# In[64]:


t = not (d)
type(t)


# In[65]:


print(t)


# In[66]:


not(a and b) or (c or d)


# # Comparisons

# In[69]:


print(4<5)


# In[71]:


c = 2<3
print(type(c))
print(c)


# In[74]:


d = 3 == 4
print(d)


# In[75]:


3 == 3.0


# In[76]:


x = 4
y = 9
z = 8.3
r = -3


# In[80]:


(x<y) and (z<y) or (r == x)


# In[81]:


(r==x) and (x<y) or (z>y)


# Exercise

# print((not(2!=3) and True) or (False and True))
# 

# In[82]:


print((not(2!=3) and True) or (False and True))


# # Some Useful Functions

# round()

# The round function rounds the input value to a specified number of places or to the nearest integer

# In[83]:


print(round(5.6234))


# In[86]:


print(round(5.324653, 3))


# divmod()

# divmod(x,y) outputs the quotient and the reminder in a tuple( We will see what a tuple is)
# 

# In[87]:


divmod(24,9)


# In[88]:


divmod(22,10)


# In[93]:


G = divmod(34,9)


# In[92]:


type(G)


# In[94]:


print(G)


# In[95]:


G[0]


# In[96]:


G[1]


# is instance()
# 

# returns True, if the first argument is an instance of that class. 
# Multiple classes can also be checked at once.

# In[2]:


isinstance(2, int)


# In[3]:


isinstance(9.3, int)


# In[5]:


isinstance(9.3, (int, float))


# In[ ]:


isinstance(2+2j, (int, float, complex))


# In[ ]:


power(x,y,z)


# x raise to the power y and remainder by z

# In[8]:


pow(2,4)


# In[9]:


2**4


# In[11]:


pow(2,4,7)


# input()

# In[ ]:


x = input("Enter a number  :")


# In[ ]:


type(x)


# In[ ]:


x = int(x)


# In[ ]:


print (x - 24)


# In[ ]:





# In[ ]:




