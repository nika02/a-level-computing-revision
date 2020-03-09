# recursive version
def binary_search_recursion(array, target, left, right):
    if right >= 1:  # check base case
        middle = (right - left) // 2 + 1
        
        if array[middle] == target:
            return mid
        elif array[middle] > target: # target is smaller than the middle element
            return binary_search_recursion(array, target, left, middle - 1)  # calls function again to search for the left subarray
        else:  # target is larger than the middle element
            return binary_search_recursion(array, target, middle + 1, right)
            
    else:
        return "Not found"
        
        
# iterative verison
