import time

def counting_sort(arr, exp1):
    """
    Counting Sort (Subroutine for Radix Sort):
    This is used to sort elements by a specific digit (unit, tens, etc.)
    Time Complexity: O(n) - where n is the size of the input array.
    Space Complexity: O(n) - Requires extra space for output array.
    """
    n = len(arr)
    output = [0] * n  # Output array that will hold the sorted array
    count = [0] * 10  # Count array to store the count of occurrences of each digit

    # Count occurrences of digits
    for i in range(n):
        index = arr[i] // exp1  # Find the digit to sort by
        count[index % 10] += 1

    # Update count to contain actual position of the digit
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array using the count array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Radix Sort Algorithm:
    Time Complexity: O(nk), where n is the number of elements and k is the number of digits in the largest number.
    Space Complexity: O(n + k) - Extra space for the output and counting arrays.
    Radix Sort sorts numbers digit by digit, starting from the least significant digit using counting sort as a subroutine.
    """
    max1 = max(arr)  # Find
