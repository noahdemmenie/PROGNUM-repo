#!/usr/bin/env python
# coding: utf-8

# Answers for Week 2
# 
# * Name: Noah Demmenie
# * Username: ndemmenie
# * Student s-number: S6294588
# * Group (AS1, etc.): AS3

# **Question 3.1 : Average calculator:**

# In[27]:


# List of masses

masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]

# Only print the masses smaller or equal of the mass of the moon

new_masses = []
for i in masses:
    if i > masses[-2]:
        new_masses.append(i)
print(f"New masses = {new_masses}")

# Only print the last 5 masses

indices = slice(-5,None,1)
sliced_masses = masses[indices]
print(f"Last 5 masses = {sliced_masses}")

# Avererge of last 5 masses

sum_sliced_masses = sum(sliced_masses)
len_sliced_masses = len(sliced_masses)
print(f"Average of last 5 masses = {sum_sliced_masses / len_sliced_masses}")


# In[ ]:




