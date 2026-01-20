"""
Binary Search Algorithm

Idea:
Binary search is an efficient searching algorithm that works on 
sorted arrays. It repeatedly divides the search interval in half 
by comparing the target value with the middle element.

How it works:
1. Find the middle element of the sorted array
2. If middle element equals target, return its index
3. If target is less than middle, search in the left half
4. If target is greater than middle, search in the right half
5. Repeat until target is found or search space is exhausted

Prerequisites:
- Array must be sorted in ascending order

Time Complexity:
Best Case:  O(1)      (element found at middle)
Average:    O(log n)
Worst Case: O(log n)  (element not found)

Space Complexity:
O(1) → Iterative approach (no extra space)
"""

def binary_search(sorted_list, target):
    """
    Searches for a target element in a sorted list using Binary Search.
    
    Parameters:
    sorted_list (list): Sorted list of elements to search through
    target: Element to search for
    
    Returns:
    int: Index of the target element if found, -1 otherwise
    """
    size = len(sorted_list)
    start = 0
    end = size - 1
    
    while start <= end:
        # Find the middle index
        mid = (start + end) // 2
        
        # Check if target is present at mid
        if sorted_list[mid] == target:
            return mid  # Found the target
        
        # If target is smaller, ignore right half
        elif sorted_list[mid] > target:
            end = mid - 1
        
        # If target is larger, ignore left half
        elif sorted_list[mid] < target:
            start = mid + 1
    
    # Target not found in the list
    return -1


# ---------------------- Testing ----------------------
if __name__ == "__main__":
    sorted_list = [10, 23, 45, 70, 88, 95, 100]
    target = 70
    
    print("Sorted array:", sorted_list)
    print("Target:", target)
    
    result = binary_search(sorted_list, target)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array")