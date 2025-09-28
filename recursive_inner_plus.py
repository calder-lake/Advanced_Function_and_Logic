#!/usr/bin/env python
# coding: utf-8

# In[49]:


input_list = [[1], [2,3,4,5, [3,2,1]],[4]]


# In[50]:


def find_innermost_list(nested_list, depth=0):
    """
    Parameters:
    nested_list (list): A potentially deeply nested list structure.
    Returns:
    tuple: (deepest list, depth)
    """
    # Start by assuming the current list is the deepest
    deepest = (nested_list, depth)
    #If the current list contains other sublists, explore them further by increasing depth
    for item in nested_list:
        if isinstance(item, list):
            candidate = find_innermost_list(item, depth + 1)
            #Update deepest list and depth if candidate is deeper
            if candidate[1] > deepest[1]:
                deepest = candidate
    return deepest


# In[51]:


def just_innermost_list(nested_list):
    """
    Parameters:
    nested_list (list): A potentially deeply nested list structure.
    Returns:
    list: innermost list
    """
    return find_innermost_list(nested_list)[0]


# In[52]:


def innermost_list_plus(nested_list):
    """
    Parameters:
    nested_list (list): A potentially deeply nested list structure.
    Returns:
    list: innermost list with 1 added to each element
    """
    result = just_innermost_list(nested_list)
    result = [(i + 1) for i in result]
    return result


# In[53]:


just_innermost_list(input_list)


# In[54]:


import sys
import ast
if __name__ == "__main__":
    #Ensure an input list is provided following the Python script in quotations, provide instructions if not.
    if len(sys.argv) < 2:
        print("Usage: python3 recursive_inner_plus.py \"[your, nested, list]\"")
        sys.exit(1)

    input_string = sys.argv[1]

    try:
        # Safely convert the input string to a Python list and verify that it is formatted as a list.
        nested_list = ast.literal_eval(input_string)
        if not isinstance(nested_list, list):
            raise ValueError

        result = innermost_list_plus(nested_list)
        print("Innermost list:", result)
    except (SyntaxError, ValueError):
        print("Error: Invalid list format. Make sure to use valid Python list syntax.")


# In[ ]:




