def binary_search(arr, target):
    # Check if the array is empty
    if len(arr) == 0:
        return 0, None  # If the array is empty, return 0 iterations and None

    # Initialize low and high indices for binary search
    low_index = 0
    high_index = len(arr) - 1
    iterations = 0  # Counter to track the number of iterations

    # Perform binary search
    while low_index <= high_index:
        iterations += 1  # Increment the iteration counter

        mid_index = (low_index + high_index) // 2  # Calculate the middle index
        mid_value = arr[mid_index]  # Get the value at the middle index

        # Check if the target is less than, greater than, or equal to the middle value
        if mid_value < target:
            low_index = mid_index + 1  # Update low index for the right half of the array
        elif mid_value > target:
            high_index = mid_index - 1  # Update high index for the left half of the array
        else:
            return iterations, mid_value  # Return the number of iterations and the found value

    # If the target is not found, return the number of iterations and the upper bound
    return iterations, arr[low_index] if low_index < len(arr) else None


# Test the binary search function
arr = [1.4, 1.5, 3.5, 3.9, 4.7, 6.7]
for target in [1.1, 3.5, 5.2, 6.9, 9.9]:
    print(binary_search(arr, target))