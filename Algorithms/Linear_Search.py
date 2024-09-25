import time

def linear_search(arr, target):
    """
    Linear Search Algorithm:
    Time Complexity: O(n) in all cases (Best, Average, and Worst) where n is the size of the array.
    Space Complexity: O(1) - No additional space is required.
    Linear Search is a simple search algorithm where we go through each element in the array until we find the target.
    """
    start_time = time.time()  # Start the timer
    for i in range(len(arr)):
        if arr[i] == target:  # Check if the current element matches the target
            end_time = time.time()  # End the timer if the element is found
            print(f"Linear Search completed in {end_time - start_time:.6f} seconds.")
            return i  # Return the index of the found element
    end_time = time.time()  # End the timer if the element is not found
    print(f"Linear Search completed in {end_time - start_time:.6f} seconds.")
    return -1  # Return -1 if the target is not found

# Example usage:
arr = list(map(int, input("Enter the array (space-separated): ").split()))
target = int(input("Enter the element to search: "))  # Input the element to search
result = linear_search(arr, target)  # Perform linear search
if result != -1:
    print(f"Element found at index {result}.")  # If element is found
else:
    print("Element not found.")  # If element is not found
