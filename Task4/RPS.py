#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

# User input

user_input = input("Type R for rock, P for paper or S for scissors:")

# Computer input

computer_input = np.random.choice(['R', 'P', 'S'])

print(f"Computer chose: {computer_input}")

# Judging result

if user_input == computer_input:
    print("Tie!")
elif user_input == 'R' and computer_input == 'P' or user_input == 'S' and computer_input == 'R' or user_input == 'P' and computer_input == 'S' :
    print("You lose!")
else:
    print("You win!")

