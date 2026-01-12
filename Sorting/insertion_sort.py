"""
Insertion Sort Algorithm

Idea:
We divide the array into two parts:
1. Sorted part (left side)
2. Unsorted part (right side)

We pick one element from the unsorted part and insert it
into its correct position in the sorted part.

Time Complexity:
Best Case:  O(n)    (already sorted)
Average:    O(n^2)
Worst Case: O(n^2)

Space Complexity:
O(1) → In-place sorting
"""


def insertion_sort(arr):
    """
    Sorts the array using Insertion Sort.

    Parameters:
    arr (list): List of integers to be sorted

    Returns:
    list: Sorted list
    """

    # Loop from the second element to the end of the array
    for i in range(1, len(arr)):

        # Current element to be placed at correct position
        key = arr[i]

        # Index of the previous element
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key
        # one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]   # shift element to the right
            j -= 1

        # Place key at its correct position
        arr[j + 1] = key

    return arr


# ---------------------- Testing ----------------------

if __name__ == "__main__":
    nums = [5, 3, 8, 6, 2]
    print("Original array:", nums)
    sorted_nums = insertion_sort(nums)
    print("Sorted array:", sorted_nums)