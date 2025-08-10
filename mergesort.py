def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2  # Find the middle point
    left_half = merge_sort(arr[:mid])  # Sort the left half
    right_half = merge_sort(arr[mid:])  # Sort the right half

    return merge(left_half, right_half)  # Merge the sorted halves

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Merge the two halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # If there are remaining elements in left or right, add them
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [3, 9, 10, 27, 38, 43, 82]
