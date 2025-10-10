#!/usr/bin/env python
# coding: utf-8

# In[11]:


def filter_list(input_list, number):
    """
    Parameters:
    input_list: a list of elements
    number: int for threshold value above which elements are excluded
    Returns:
    list with elements removed with values above the threshold
    """
    list = input_list
    j = []
    for item in list:
        if item <= number:
            j.append(item)
        else:
            continue
    return j


# In[7]:


some_list = [1,2,3,4,5,4,7,8,6,3,9]


# In[8]:


filter_list(some_list, 6)


# In[13]:


import sys
import ast
if __name__ == "__main__":
    #Ensure an input list is provided following the Python script in quotations, provide instructions if not.
    if len(sys.argv) < 3:
        print("Usage: python3 function_filter_list.py \"[list, of, values]\" number(int)")
        sys.exit(1)

    list_arg = sys.argv[1]
    number_arg = sys.argv[2]

    try:
        # Safely convert the input string to a Python list and verify that it is formatted as a list.
        input_list = ast.literal_eval(list_arg)
        if not isinstance(input_list, list):
            raise ValueError("First argument must be a list.")

        number = int(number_arg)

        result = filter_list(input_list, number)
        print("Filtered list:", result)
    except (SyntaxError, ValueError):
        print("Error: Invalid list format. Make sure to use valid Python list syntax and an integer for the second argument.")


# In[ ]:




