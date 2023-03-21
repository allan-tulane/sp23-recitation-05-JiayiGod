import random, time
import tabulate
import sys
import matplotlib.pyplot as plt
from math import log2

sys.setrecursionlimit(100000)

def ssort(a):     
    for i in range(len(a) - 1):
        minIndex = i
        for j in range(i + 1, len(a)):
            if a[j] < a[minIndex]:
                minIndex = j
        if i != minIndex:
            a[i], a[minIndex] = a[minIndex], a[i]
    return a
    pass
    
def qsort(a, pivot_fn):
    left=[]
    right=[]
    middle=[]
    if(len(a)<=1):
        return a
    p=pivot_fn(a)
    for num in a:
        if num<p:
            left.append(num)
        elif num==p:
            middle.append(num)
        else:
            right.append(num)
    return  qsort(left,pivot_fn)+middle+qsort(right,pivot_fn)
    pass
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000

def compare_sort(sizes=[10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = lambda mylist:qsort(mylist,lambda list:list[0])
    qsort_random_pivot = lambda mylist:qsort(mylist,lambda list:list[random.randint(0,len(list)-1)])
    selection_sort=lambda mylist:ssort(mylist)
    tim_sort = lambda list:sorted(list)
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(tim_sort, mylist),            
        ])
    # plt.figure()
    # plt.plot(sizes, [r[1] for r in result], 'o-', label='qsort_fixed_pivot')
    # plt.plot(sizes, [r[2] for r in result], 'o-', label='qsort_random_pivot')
    # plt.plot(sizes, [r[3] for r in result], 'o-', label='selection_sort')
    # plt.legend()
    # plt.show()
    return result

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot','tim_sort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())
    

random.seed()
test_print()

