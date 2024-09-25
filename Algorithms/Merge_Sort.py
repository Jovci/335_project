import time

def merge_sort(arr):
    """
    Merge Sort Algorithm:
    Time Complexity: O(n log n) in all cases (Best, Average, and Worst).
    Space Complexity: O(n) - Requires additional space for merging.
    Merge Sort is a divide-and-conquer algorithm that splits the array into halves, recursively sorts each half, and merges the sorted halves.
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle point
        left_half = arr[:mid]  # Split the array into left half
        right_half = arr[mid:]  # Split the array into right half

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        i = j = k = 0  # Initialize pointers for left_half, right_half, and arr

        # Merge the sorted halves into arr
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements of left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements of right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def merge_sort_with_timer(arr):
    start_time = time.time()  # Start the timer
    merge_sort(arr)  # Perform merge sort
    end_time = time.time()  # End the timer
    print(f"Merge Sort completed in {end_time - start_time:.6f} seconds.")  # Display the execution time
    return arr

# Example usage:
arr = list(map(int, input("Enter the array to sort (space-separated): ").split()))
print("Unsorted array:", arr)
sorted_arr = merge_sort_with_timer(arr)  # Sort the array using merge sort
print("Sorted array:", sorted_arr)
