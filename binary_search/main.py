from binary_search import BinarySearch, normal_search
from utils import Generator_Data, plot_elapsed_times


def main():
    # add more values to the sizes list to test the performance of the functions with larger inputs
    sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
    for size in sizes:
        data = Generator_Data.list_generator(size)
        target = size // 2
        BinarySearch.search(data, target)
        normal_search(data, target)

    plot_elapsed_times()


if __name__ == "__main__":
    main()
