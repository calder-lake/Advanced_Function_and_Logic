#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. 
#This is to be done with a while loop. Note: the input will contain only integers or lists. 
#As an example:
#input_list = [1,2,3,4,[5,6,7,[8,9]]]
#your_py_program.py input_list
#will produce:
#[9,10]
#That is [8, 9] (the inner most list) plus 1 -> [9, 10]


# In[71]:


input_list = [5,6,7,[2,3,[1,0,-1]]]


# In[60]:


def find_innermost_list(nested_list):
    """
    Parameters:
    nested_list (list): A potentially deeply nested list structure.
    Returns:
    list: The innermost list within the input.
    """
    # Initialize the stack as a tuple with the outermost list and its starting depth (0)
    # The stack holds tuples of (current_list, current_depth)
    stack = [(nested_list, 0)]
    #Track the deepest sublist and its depth
    deepest = (nested_list, 0)

    while stack:
        #Pop the last added sublist and record its depth starting at 0
        current, depth = stack.pop()
        #Update the deepest list if the current one is nested deeper
        if depth > deepest[1]:
            deepest = (current, depth)

        #If the current list contains other sublists, explore them further
        if isinstance(current, list):
            for item in current:
                if isinstance(item, list):
                    #Add sublist and its depth (one level deeper) to the stack
                    stack.append((item, depth + 1))
    #Return the list that was found to be deepest in the nested structure
    return deepest[0]


# In[61]:


find_innermost_list(input_list)


# In[62]:


def inner_plus_one(nested_list):
    """
    Parameters:
    nested_list (list): A potentially deeply nested list structure.
    Returns:
    list: innermost list within the input with 1 added to each element
    """
    result = find_innermost_list(nested_list)
    result = [(i + 1) for i in result]
    return result



# In[63]:


inner_plus_one(input_list)


# In[72]:


import sys
import ast
if __name__ == "__main__":
    #Ensure an input list is provided following the Python script in quotations, provide instructions if not.
    if len(sys.argv) < 2:
        print("Usage: python3 while_inner_plus.py \"[your, nested, list]\"")
        sys.exit(1)

    input_string = sys.argv[1]

    try:
        # Safely convert the input string to a Python list and verify that it is formatted as a list.
        nested_list = ast.literal_eval(input_string)
        if not isinstance(nested_list, list):
            raise ValueError

        result = inner_plus_one(nested_list)
        print("Innermost list:", result)
    except (SyntaxError, ValueError):
        print("Error: Invalid list format. Make sure to use valid Python list syntax.")


# In[ ]:




