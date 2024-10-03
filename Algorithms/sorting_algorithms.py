import time
import random

# Sorting Algorithms and Linear Search

def bubble_sort(arr):
    """
    Bubble Sort Algorithm:
    - Compares adjacent elements and swaps them if they are in the wrong order.
    - Repeatedly passes through the list until no more swaps are needed (i.e., the list is sorted).
    - Time Complexity: O(n^2) in Worst and Average Case, O(n) in Best Case (when array is already sorted).
    - Space Complexity: O(1) - In-place sorting.
    """
    n = len(arr)
    for i in range(n):
        swapped = False  # Flag to detect if any swap occurs in this pass
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # No swaps mean the array is already sorted
    return arr

def merge_sort(arr):
    """
    Merge Sort Algorithm:
    - A Divide and Conquer algorithm that recursively divides the array in half, sorts the halves, and merges them.
    - Time Complexity: O(n log n) for all cases.
    - Space Complexity: O(n) - Not in-place sorting.
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the midpoint
        left_half = arr[:mid]  # Left half of the array
        right_half = arr[mid:]  # Right half of the array

        # Recursively split and sort the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two halves back together in sorted order
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements from left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements from right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    """
    Quick Sort Algorithm:
    - Uses a pivot to partition the array into subarrays, sorting them recursively.
    - Time Complexity: O(n log n) on average, O(n^2) in the worst case.
    - Space Complexity: O(log n) due to recursion.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot
    # Recursively sort left and right subarrays, and combine them with middle
    return quick_sort(left) + middle + quick_sort(right)

def counting_sort(arr, exp1):
    """
    Helper function for Radix Sort - Counting Sort based on significant digits (exp).
    """
    n = len(arr)
    output = [0] * n  # Output array to hold the sorted numbers
    count = [0] * 10  # Count array to store occurrences of digits

    # Store count of occurrences
    for i in range(n):
        index = arr[i] // exp1
        count[(index) % 10] += 1

    # Update count to store cumulative sum
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1

    # Copy the sorted numbers back to the original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Radix Sort Algorithm:
    - Sorts numbers by processing individual digits starting from the least significant digit.
    - Time Complexity: O(d*(n+k)), where d is the number of digits, n is the number of elements, and k is the base.
    - Space Complexity: O(n+k).
    """
    max1 = max(arr)  # Find the maximum number to determine the number of digits
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def linear_search(arr, target):
    """
    Linear Search Algorithm:
    - Iterates through the array to find the target element.
    - Time Complexity: O(n) in the worst case.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the found element
    return -1  # Return -1 if the element is not found

# Function to measure the execution time of algorithms
def measure_execution_time(func, *args):
    """
    Measures the time taken by a function to execute.
    Uses time.perf_counter() for high-precision timing.
    """
    start_time = time.perf_counter()  # Start the timer
    result = func(*args)  # Call the function
    end_time = time.perf_counter()  # End the timer
    return result, end_time - start_time  # Return result and elapsed time

# Function to get array input from the user (manual or random generation)
def get_array_input():
    """
    Prompts the user to input an array manually or generate a random array.
    Returns the array entered/generated.
    """
    choice = input("Do you want to input the array manually or generate a random array? (manual/random): ").strip().lower()

    if choice == "manual":
        # Manual input of array elements
        array_str = input("Enter the array elements separated by spaces: ").strip()
        arr = list(map(int, array_str.split()))
    elif choice == "random":
        # Generate a random array of user-specified size
        size = int(input("Enter the size of the random array: ").strip())
        arr = [random.randint(1, 1000) for _ in range(size)]
    else:
        # Handle invalid input
        print("Invalid input. Please try again.")
        return get_array_input()
    
    return arr

# Function to get target element for linear search
def get_target_input():
    """
    Prompts the user to input the target element for the linear search.
    Returns the target element.
    """
    target = int(input("Enter the target element for Linear Search: ").strip())
    return target

def main():
    """
    Main function to run the sorting and search algorithms with time comparisons.
    - Prompts the user to input or generate an array.
    - Performs sorting and linear search, and prints the time taken by each algorithm.
    """
    # Get the array from the user
    arr = get_array_input()
    print(f"Original Array: {arr}")

    # Get target element for linear search
    target = get_target_input()

    # Measure time for each sorting algorithm and linear search
    sorted_arr, bubble_sort_time = measure_execution_time(bubble_sort, arr.copy())
    print(f"Bubble Sort: {sorted_arr}, Time: {bubble_sort_time:.6f} seconds")

    sorted_arr, merge_sort_time = measure_execution_time(merge_sort, arr.copy())
    print(f"Merge Sort: {sorted_arr}, Time: {merge_sort_time:.6f} seconds")

    sorted_arr, quick_sort_time = measure_execution_time(quick_sort, arr.copy())
    print(f"Quick Sort: {sorted_arr}, Time: {quick_sort_time:.6f} seconds")

    sorted_arr, radix_sort_time = measure_execution_time(radix_sort, arr.copy())
    print(f"Radix Sort: {sorted_arr}, Time: {radix_sort_time:.6f} seconds")

    # Perform Linear Search and measure time
    index, linear_search_time = measure_execution_time(linear_search, arr, target)
    if index != -1:
        print(f"Linear Search: Element found at index {index}, Time: {linear_search_time:.6f} seconds")
    else:
        print(f"Linear Search: Element not found, Time: {linear_search_time:.6f} seconds")

if __name__ == "__main__":
    main()
