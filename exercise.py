"""
Generate random lists of integers for various sizes (e.g., 100, 1000, 10000). 
Use the timeit module to measure the runtime of Merge Sort and Quick Sort on each list. 
Create a comparative analysis, including runtime graphs using matplotlib, 
to visualize the efficiency of both sorting algorithms for different input sizes.
"""

import timeit
from random import randint
from sorting_techniques import pysort
import matplotlib.pyplot as plt

class Generator:
    def __init__(self):
        self.list = []

    def generate(self, size):
        if list != []:
            self.list.clear()
        for i in range(size):
            self.list.append(randint(1, 9000000))
        return self.list


if __name__ == '__main__':
    generator = Generator()
    init_number = 10
    final_number = 1250
    step = 10
    elements_quantity = range(init_number, final_number, step) # this is my X axis
    merge_sort_times = []
    quick_sort_times = []
    sortObj = pysort.Sorting()

    for size in elements_quantity:
        random_list = generator.generate(size)
        merge_sort_times.append(timeit.timeit('sortObj.mergeSort(random_list)', globals=globals(), number=1))
        
        min_value = min(random_list)
        min_value_index = random_list.index(min_value)
        pivot = len(random_list) // 2
        quick_sort_times.append(timeit.timeit('sortObj.quickSort(random_list,min_value_index,pivot)', globals=globals(), number=1))

    plt.plot(elements_quantity, merge_sort_times, label='Merge Sort')
    plt.plot(elements_quantity, quick_sort_times, label='Quick Sort')
    plt.xlabel('Elements Quantity in list')
    plt.ylabel('Time')
    plt.title('Merge Sort vs Quick Sort')
    plt.legend()
    plt.show()

