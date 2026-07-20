from utils.timer import time_function_decorator_global

#static class for binary search algorithm

class BinarySearch:
    @staticmethod
    @time_function_decorator_global
    def search(list, target):
        """
        Perform a binary search on a sorted list to find the index of the target value.

        Parameters:
        list (list): A sorted list of elements to search.
        target: The value to search for in the list.

        Returns:
        int: The index of the target value if found, otherwise -1.
        """

        list_size = len(list)

        low_index = 0
        high_index = list_size - 1

        attempts = 0

        while low_index <= high_index:

            attempts += 1

            mid_index = (low_index + high_index) // 2
            attempted_value = list[mid_index]

            if attempted_value == target:
                return mid_index, attempts
            elif attempted_value < target:
                low_index = mid_index + 1
            else:
                high_index = mid_index - 1

        return None
    
    @staticmethod
    @time_function_decorator_global
    def search_recursive(list, target):
        """
        Perform a binary search on a sorted list to find the index of the target value.

        Parameters:
        list (list): A sorted list of elements to search.
        target: The value to search for in the list.

        Returns:
        int: The index of the target value if found, otherwise -1.
        """

        list_size = len(list)

        low_index = 0
        high_index = list_size - 1

        attempts = 0

        def recursive_helper(low_index, high_index):
            nonlocal attempts
            attempts += 1
            mid_index = (low_index + high_index) // 2

            attempted_value = list[mid_index]

            if attempted_value == target:
                return mid_index
            
            if attempted_value > target:
                return recursive_helper(low_index, mid_index-1)
            
            if attempted_value < target:
                return recursive_helper(mid_index + 1, high_index)
            
        return recursive_helper(low_index, high_index)

@time_function_decorator_global
def normal_search(list, target):
    """
    Perform a linear search on a list to find the index of the target value.

    Parameters:
    list (list): A list of elements to search.
    target: The value to search for in the list.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """

    attempts = 0

    for x in range(len(list)):
        attempts += 1
        if list[x] == target:
            return x, attempts
        
    return None

