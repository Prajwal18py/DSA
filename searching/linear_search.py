"""
Linear Search Algorithm

Idea:
Linear search is the simplest searching algorithm that checks every 
element in the list sequentially until the target element is found 
or the end of the list is reached.

How it works:
1. Start from the first element of the array
2. Compare each element with the target value
3. If a match is found, return the index
4. If no match is found after checking all elements, return -1

Time Complexity:
Best Case:  O(1)    (element found at first position)
Average:    O(n)
Worst Case: O(n)    (element not found or at last position)

Space Complexity:
O(1) → No extra space needed
"""

def linear_search(my_list, target):
    """
    Searches for a target element in the list using Linear Search.
    
    Parameters:
    my_list (list): List of elements to search through
    target: Element to search for
    
    Returns:
    int: Index of the target element if found, -1 otherwise
    """
    size = len(my_list)
    
    # Traverse through all elements
    for index in range(size):
        # Check if current element matches the target
        if my_list[index] == target:
            return index
    
    # Target not found in the list
    return -1


# ---------------------- Testing ----------------------
if __name__ == "__main__":
    my_list = [10, 23, 45, 70, 11]
    target = 23
    
    print("Array:", my_list)
    print("Target:", target)
    
    result = linear_search(my_list, target)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array")