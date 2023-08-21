def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n-1):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
my_list = [5,9,6,4,7,2,3,1,8]
bubble_sort(my_list)
print("Sorted array:", my_list)