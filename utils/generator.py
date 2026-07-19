#static class for generating random data

class Generator_Data:
    @staticmethod
    def list_generator(size):
        """
        Generate a sorted list of integers from 0 to size - 1.

        Parameters:
        size (int): The size of the list to generate.

        Returns:
        list: A sorted list of integers.
        """
        return list(range(size))