import pygame
import random
import math
import time

# Initialize Pygame
pygame.init()

# Class to store and manage drawing information for the sorting visualization
class DrawInformation:
    # Color constants for the bars and background
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BLUE = 0, 0, 255
    BACKGROUND_COLOR = WHITE

    # Gradient colors to visually differentiate bars
    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    # Font settings for UI elements
    FONT = pygame.font.SysFont('sanserrif', 20)
    LARGE_FONT = pygame.font.SysFont('sanserrif', 70)

    # Padding settings for the window display
    SIDE_PAD = 100
    TOP_PAD = 150

    # Initialization function to set up the window and the list of numbers
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(lst)

    def set_list(self, lst):
        """Sets the list to be sorted and calculates necessary dimensions."""
        self.lst = lst
        self.min_val = min(lst)  # Minimum value in the list
        self.max_val = max(lst)  # Maximum value in the list
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))  # Width of each bar
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))  # Height scaling
        self.start_x = self.SIDE_PAD // 2  # X-axis starting position for bars

# Function to draw the current sorting state, including UI elements like title and controls
def draw(draw_info, algo_name, time_elapsed, sorting_completed):
    """Draws the current sorting visualization with UI elements."""
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    # Title text showing algorithm name and time elapsed (or completion message)
    if sorting_completed:
        title = draw_info.LARGE_FONT.render(f"{algo_name} - Completed sorting in {time_elapsed:.4f}s", True, draw_info.BLACK)
    else:
        title = draw_info.LARGE_FONT.render(f"{algo_name} - Time: {time_elapsed:.4f}s", True, draw_info.BLACK)

    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    # Controls instruction text
    controls_text = "R - Reset | SPACE - Start Sorting | S - Search"
    controls = draw_info.FONT.render(controls_text, True, draw_info.BLACK)
    controls_box_rect = pygame.Rect(10, 40, controls.get_width() + 20, 50)
    pygame.draw.rect(draw_info.window, draw_info.BLACK, controls_box_rect, border_radius=10)  # Border
    pygame.draw.rect(draw_info.window, draw_info.WHITE, controls_box_rect.inflate(-4, -4), border_radius=10)  # Inner background
    draw_info.window.blit(controls, (controls_box_rect.x + 10, controls_box_rect.y + 10))

    # Box for sorting algorithms and search instruction
    instruction_box_rect = pygame.Rect(10, 100, 250, 150)  # Adjust dimensions as needed
    pygame.draw.rect(draw_info.window, draw_info.BLACK, instruction_box_rect, border_radius=10)  # Border
    pygame.draw.rect(draw_info.window, draw_info.WHITE, instruction_box_rect.inflate(-4, -4), border_radius=10)  # Inner background

    # Sorting algorithm instructions
    sorting_texts = [
        "B - Bubble Sort", "M - Merge Sort",
        "Q - Quick Sort", "D - Radix Sort",
        "L - Linear Search (Click L and then S)"
    ]

    for i, text in enumerate(sorting_texts):
        sorting_instruction = draw_info.FONT.render(text, True, draw_info.BLACK)
        draw_info.window.blit(sorting_instruction, (instruction_box_rect.x + 10, instruction_box_rect.y + 10 + (i * 30)))

    # Draw the list (bars) with the updated interface
    draw_list(draw_info)
    pygame.display.update()

# Function to draw the list of bars with optional color highlights for certain bars
def draw_list(draw_info, color_positions={}, clear_bg=False):
    """Draws the list of bars representing the array."""
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD,
                      draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        color = draw_info.GRADIENTS[i % 3]
        if i in color_positions:
            color = color_positions[i]
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height - y))

        # Draw the value on top of the bar
        value_surface = draw_info.FONT.render(str(val), True, draw_info.BLACK)
        value_x = x + (draw_info.block_width // 2) - (value_surface.get_width() // 2)  # Center the text
        value_y = y - value_surface.get_height() - 5  # Position it above the bar

        # Only draw the value if it is above the top of the window
        if value_y >= draw_info.TOP_PAD:
            draw_info.window.blit(value_surface, (value_x, value_y))

    if clear_bg:
        pygame.display.update()  # Refresh the display if background is cleared

# Function to generate a random list of integers within a specified range
def generate_starting_list(n, min_val, max_val):
    """Generates a list of random integers within specified range."""
    return [random.randint(min_val, max_val) for _ in range(n)]  # Generate list of random integers

# Sorting Algorithms

def bubble_sort(draw_info):
    """
    Bubble Sort Algorithm Visualization:
    Time Complexity: O(n^2) in the worst case, O(n) in the best case (already sorted array).
    Space Complexity: O(1) as it sorts in place.
    """
    lst = draw_info.lst
    n = len(lst)

    # Bubble sort process with two loops
    for i in range(n - 1):
        for j in range(n - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            # Swap adjacent elements if they are in the wrong order
            if num1 > num2:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                # Visualize the swap by highlighting the swapped bars
                draw_list(draw_info, {j: draw_info.BLUE, j + 1: draw_info.RED}, True)
                yield True  # Yield to allow drawing the swap step
    return lst

def merge_sort(draw_info, lst, l, r):
    """
    Merge Sort Algorithm Visualization:
    Time Complexity: O(n log n) in all cases.
    Space Complexity: O(n) due to the use of auxiliary arrays.
    """
    if l >= r:
        return

    # Divide the array into two halves recursively
    mid = (l + r) // 2
    yield from merge_sort(draw_info, lst, l, mid)
    yield from merge_sort(draw_info, lst, mid + 1, r)
    yield from merge(draw_info, lst, l, mid, r)

def merge(draw_info, lst, l, mid, r):
    """
    Merge step for Merge Sort: Merges two sorted halves.
    """
    left = lst[l:mid + 1]
    right = lst[mid + 1:r + 1]

    i = j = 0
    k = l

    # Merge the two halves by comparing elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1
        # Visualize the merge process
        draw_list(draw_info, {k - 1: draw_info.BLUE}, True)
        yield True

    # Copy any remaining elements from left
    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1
        draw_list(draw_info, {k - 1: draw_info.BLUE}, True)
        yield True

    # Copy any remaining elements from right
    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1
        draw_list(draw_info, {k - 1: draw_info.BLUE}, True)
        yield True

def quick_sort(draw_info, lst, low, high):
    """
    Quick Sort Algorithm Visualization:
    Time Complexity: O(n log n) on average, O(n^2) in the worst case (already sorted array).
    Space Complexity: O(log n) due to recursion.
    """
    if low < high:
        # Partition the array and get the pivot index
        pi = yield from partition(draw_info, lst, low, high)
        # Recursively sort the elements before and after the pivot
        yield from quick_sort(draw_info, lst, low, pi - 1)
        yield from quick_sort(draw_info, lst, pi + 1, high)

def partition(draw_info, lst, low, high):
    """
    Split the array into parts based on a pivot for Quick Sort.
    """
    pivot = lst[high]
    i = low - 1

    # Rearrange elements based on the pivot
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
            draw_list(draw_info, {i: draw_info.BLUE, j: draw_info.RED}, True)
            yield True

    # Place the pivot element in its correct position
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    draw_list(draw_info, {i + 1: draw_info.BLUE, high: draw_info.RED}, True)
    yield True
    return i + 1

def counting_sort(draw_info, lst, exp):
    """
    Helper function for Radix Sort to perform Counting Sort based on significant digits.
    Time Complexity: O(n), where n is the number of elements.
    Space Complexity: O(n + k), where k is the number of digits (range of the count).
    """
    n = len(lst)
    output = [0] * n  # Output array to store sorted numbers
    count = [0] * 10  # Count array to store occurrences of each digit

    # Count occurrences of digits
    for i in range(n):
        index = lst[i] // exp
        count[index % 10] += 1
        draw_list(draw_info, {i: draw_info.BLUE}, True)
        yield True

    # Update the count array to contain positions of digits
    for i in range(1, 10):
        count[i] += count[i - 1]
        yield True

    # Build the output array by placing elements in correct positions
    i = n - 1
    while i >= 0:
        index = lst[i] // exp
        output[count[index % 10] - 1] = lst[i]
        count[index % 10] -= 1
        i -= 1
        yield True

    # Copy the output array back to the original list
    for i in range(n):
        lst[i] = output[i]
        draw_list(draw_info, {i: draw_info.GREEN}, True)
        yield True

def radix_sort(draw_info):
    """
    Radix Sort Algorithm Visualization:
    Time Complexity: O(d * (n + k)), where d is the number of digits, n is the number of elements, and k is the base.
    Space Complexity: O(n + k) due to auxiliary storage.
    """
    lst = draw_info.lst
    max1 = max(lst)  # Find the maximum number to determine the number of digits
    exp = 1

    # Perform counting sort for every digit (starting from least significant digit)
    while max1 // exp > 0:
        yield from counting_sort(draw_info, lst, exp)
        exp *= 10
    return lst

def linear_search(draw_info, target):
    """
    Linear Search Algorithm Visualization:
    Time Complexity: O(n), where n is the number of elements in the list.
    Space Complexity: O(1).
    """
    lst = draw_info.lst
    for i in range(len(lst)):
        # Highlight the current bar being compared
        draw_list(draw_info, {i: draw_info.RED}, True)
        yield True
        if lst[i] == target:
            # Highlight the found element in green
            draw_list(draw_info, {i: draw_info.GREEN}, True)
            yield True
            break
    return lst

def main():
    run = True
    clock = pygame.time.Clock()

    # Prompt the user to enter the number of elements for the list
    try:
        n = int(input("Enter the number of elements to sort: "))
    except ValueError:
        print("Invalid input. Defaulting to 200 elements.")
        n = 200  # Default to 200 elements if input is invalid

    min_val = 1
    max_val = 100

    # Generate the initial random list of numbers
    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(1280, 720, lst)
    sorting = False
    searching = False
    sorting_completed = False

    sorting_algorithm = None
    sorting_algo_name = ""
    sorting_algorithm_generator = None
    start_time = -1
    final_time = 0  # Store the final elapsed time
    target = None  # Target value for linear search

    # Main loop for the Pygame window
    while run:
        clock.tick(60)  # Set the frame rate to 60 frames per second

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
                sorting_completed = True  # Mark sorting as completed
                final_time = time.time() - start_time  # Store the final time
        elif searching:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                searching = False
                sorting_completed = True
                final_time = time.time() - start_time
        else:
            # Calculate the elapsed time during sorting/searching
            time_elapsed = final_time if sorting_completed else (time.time() - start_time if start_time != -1 else 0)
            draw(draw_info, sorting_algo_name, time_elapsed, sorting_completed)

        # Event handling for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Quit the program if the window is closed

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:  # Reset the sorting process
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
                searching = False
                sorting_completed = False  # Reset the completion flag
                start_time = -1
                sorting_algo_name = ""
                final_time = 0  # Reset the final time
                target = None

            elif event.key == pygame.K_SPACE and not sorting and not searching:
                if sorting_algorithm is None:
                    continue  # No sorting algorithm selected
                sorting = True
                sorting_completed = False
                start_time = time.time()  # Start the timer

                # Initialize the appropriate sorting algorithm
                if sorting_algo_name == "Merge Sort":
                    sorting_algorithm_generator = sorting_algorithm(draw_info, draw_info.lst, 0, len(draw_info.lst) - 1)
                elif sorting_algo_name == "Quick Sort":
                    sorting_algorithm_generator = sorting_algorithm(draw_info, draw_info.lst, 0, len(draw_info.lst) - 1)
                else:
                    sorting_algorithm_generator = sorting_algorithm(draw_info)

            elif event.key == pygame.K_s and not sorting and not searching:
                if sorting_algorithm is None or sorting_algo_name != "Linear Search":
                    continue  # Linear Search not selected
                target_input = input("Enter the target value to search for: ")
                try:
                    target = int(target_input)
                except ValueError:
                    print("Invalid input. Please enter an integer.")
                    continue
                searching = True
                sorting_completed = False
                start_time = time.time()  # Start the timer
                sorting_algorithm_generator = sorting_algorithm(draw_info, target)

            # Set the sorting algorithm based on user input
            elif event.key == pygame.K_b and not sorting and not searching:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"
                start_time = -1

            elif event.key == pygame.K_m and not sorting and not searching:
                sorting_algorithm = merge_sort
                sorting_algo_name = "Merge Sort"
                start_time = -1

            elif event.key == pygame.K_q and not sorting and not searching:
                sorting_algorithm = quick_sort
                sorting_algo_name = "Quick Sort"
                start_time = -1

            elif event.key == pygame.K_d and not sorting and not searching:
                sorting_algorithm = radix_sort
                sorting_algo_name = "Radix Sort"
                start_time = -1

            elif event.key == pygame.K_l and not sorting and not searching:
                sorting_algorithm = linear_search
                sorting_algo_name = "Linear Search"
                start_time = -1

    pygame.quit()  # Quit Pygame when the program ends


# Run the main function
if __name__ == "__main__":
    main()
