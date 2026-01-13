"""
Bubble Sort Algorithm

Idea:
Bubble sort works by repeatedly comparing adjacent elements and 
swapping them if they are in the wrong order. The largest element 
"bubbles up" to its correct position in each pass.

How it works:
1. Compare adjacent elements
2. Swap if they are in wrong order
3. After each pass, the largest element reaches its final position
4. Repeat until the entire array is sorted

Time Complexity:
Best Case:  O(n)    (already sorted, with optimization)
Average:    O(n^2)
Worst Case: O(n^2)

Space Complexity:
O(1) → In-place sorting
"""

def bubble_sort(arr):
    """
    Sorts the array using Bubble Sort.
    
    Parameters:
    arr (list): List of integers to be sorted
    
    Returns:
    list: Sorted list
    """
    n = len(arr)
    
    # Traverse through all array elements
    for passes in range(n):
        # Last 'passes' elements are already in place
        for j in range(0, n - 1 - passes):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if current element is greater than next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


# ---------------------- Testing ----------------------
if __name__ == "__main__":
    unsorted_list = [12, 25, 11, 34, 90, 22]
    print("Original array:", unsorted_list)
    
    sorted_list = bubble_sort(unsorted_list)
    print("Sorted array:", sorted_list)