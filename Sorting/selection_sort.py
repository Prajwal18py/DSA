"""
Selection Sort Algorithm

Idea:
Selection sort divides the array into two parts:
1. Sorted part (left side)
2. Unsorted part (right side)

In each iteration, we find the minimum element from the unsorted 
part and swap it with the first element of the unsorted part.

How it works:
1. Find the minimum element in the unsorted portion
2. Swap it with the first element of the unsorted portion
3. Move the boundary between sorted and unsorted portions one step right
4. Repeat until the entire array is sorted

Time Complexity:
Best Case:  O(n^2)
Average:    O(n^2)
Worst Case: O(n^2)

Space Complexity:
O(1) → In-place sorting
"""

def selection_sort(arr):
    """
    Sorts the array using Selection Sort.
    
    Parameters:
    arr (list): List of integers to be sorted
    
    Returns:
    list: Sorted list
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n - 1):
        # Find the minimum element in remaining unsorted array
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


# ---------------------- Testing ----------------------
if __name__ == "__main__":
    unsorted_list = [12, 15, 11, 34, 90, 22]
    print("Original array:", unsorted_list)
    
    sorted_list = selection_sort(unsorted_list)
    print("Sorted array:", sorted_list)