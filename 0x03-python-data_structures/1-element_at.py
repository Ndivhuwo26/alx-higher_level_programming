#!/usr/bin/python3
1-element_at.py

    """Retrieve the element from list."""

#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    return my_list[idx]

