def linear_search(array, target):
    for element in range(len(array)):  # loops through every element in the given array
        if array[element] == target:
            return element  # returns index of where the element is found in the given array
        else:
            return "Not Found"
            
linear_search([2, 4, 5, 3, 1], 4)  # output should be 1
linear_search([2, 5, 3, 1, 7], 9) # output should be "Not found"
