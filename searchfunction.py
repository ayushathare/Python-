def search(lst, target):
    """
    Search for a target element in a list.
    
    Args:
        lst (list): The list to be searched.
        target: The element to search for.
    
    Returns:
        int: The index of the target element if found, otherwise returns -1.
    """
    for index, item in enumerate(lst):
        if item == target:
            return index
    return -1

my_list = [1, 2, 3, 4, 5]
target_element = 3
result = search(my_list, target_element)
if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found.")
