#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    mynew_list = my_list.copy()
    if idx < 0 or idx >= (len(my_list)):
        return (mynew_list)
    else:
        mynew_list[idx] = element
        return (mynew_list)
