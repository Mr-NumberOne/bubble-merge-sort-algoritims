def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    merged = merge(left_half, right_half)
    
    return merged

def merge(left, right):
    merged = []
    i = j = 0
    
    # Compare elements from the left and right halves and merge them
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Append any remaining elements from the left and right halves
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

# Example usage
my_list = [4,1,7,5,3,2,6]
sorted_list = merge_sort(my_list)
print("Sorted array:", sorted_list)