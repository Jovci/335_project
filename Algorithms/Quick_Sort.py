import time

def quick_sort(arr):
    """
    Quick Sort Algorithm:
    Time Complexity: O(n log n) on Average, O(n^2) in Worst Case (e.g., when the pivot is always the smallest or largest element).
    Space Complexity: O(log n) - Due to recursion.
    Quick Sort is a divide-and-conquer algorithm that picks a pivot and partitions the array into two halves, then recursively sorts the two halves.
    """
    if len(arr) <= 1:
        return arr  # Base case: If the array has 1 or 0 elements, it's already sorted

    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot (can be optimized)
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort and combine the results

def quick_sort_with_timer(arr):
    start_time = time.time()  # Start the timer
    sorted_arr = quick_sort(arr)  # Perform quick sort
    end_time = time.time()  # End the timer
    print(f"Quick Sort completed in {end_time - start_time:.6f} seconds.")  # Display the execution time
    return sorted_arr

# Example usage:
arr = list(map(int, input("Enter the array to sort (space-separated): ").split()))
print("Unsorted array:", arr)
sorted_arr = quick_sort_with_timer(arr)  # Sort the array using quick sort
print("Sorted array:", sorted_arr)
