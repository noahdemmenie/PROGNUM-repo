#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Sirius data
apparentMagnitude = -1.46
absoluteMagnitude = 1.45

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

m = apparentMagnitude
M = absoluteMagnitude

m = float(input("What is the apparent magnitude?"))
M = float(input("What is the absolute magnitude?"))

print(f"d = {10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164}" " ly")

