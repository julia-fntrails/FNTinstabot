#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#likes all the pics in our feed

#!pip install instapy
from instapy import InstaPy

session = InstaPy(username="fntrails", password="b1k3z99")
session.login()
session.like_by_feed(amount=10, randomize=True, unfollow=False, interact=True)
#interact=True visits the author's profile page of a certain post and likes a given
# number of their pictures, then returns to feed


# In[ ]:




