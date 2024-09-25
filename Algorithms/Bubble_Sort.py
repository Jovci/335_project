import time

def bubble_sort(arr):
    """
    Bubble Sort Algorithm:
    Time Complexity: O(n^2) in Worst and Average Case, O(n) in Best Case (when array is already sorted)
    Space Complexity: O(1) - In-place sorting.
    This is a simple comparison-based sorting algorithm that repeatedly swaps adjacent elements if they are in the wrong order.
    """
    start_time = time.time()  # Start the timer to measure execution time
    n = len(arr)
    for i in range(n):
        swapped = False  # Initialize swapped as False to detect if any swapping happened
        for j in range(0, n - i - 1):
            # Compare adjacent elements and swap if the current one is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # A swap occurred
        if not swapped:
            break  # No swaps happened, the array is already sorted
    end_time = time.time()  # End the timer
    print(f"Bubble Sort completed in {end_time - start_time:.6f} seconds.")  # Display the execution time
    return arr

# Example usage:
arr = list(map(int, input("Enter the array to sort (space-separated): ").split()))
print("Unsorted array:", arr)
sorted_arr = bubble_sort(arr)  # Sort the array using bubble sort
print("Sorted array:", sorted_arr)
