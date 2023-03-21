# CMPS 2200 Reciation 5
## Answers

**Name:**______Jiayi Xu___________________


Place all written answers from `recitation-06.md` here for easier grading.







- **1b.**

This is for random input list:

|    n |   qsort-fixed-pivot |   qsort-random-pivot |   selection_sort |
|------|---------------------|----------------------|------------------|
|  200 |               0.000 |                0.000 |            0.997 |
|  400 |               0.000 |                0.998 |            2.992 |
|  600 |               0.998 |                0.000 |            7.979 |
|  800 |               0.997 |                1.995 |           11.967 |
| 1000 |               1.995 |                0.997 |           18.950 |
| 1200 |               0.997 |                1.995 |           27.926 |
| 1400 |               1.995 |                1.671 |           36.901 |
| 1600 |               1.994 |                1.995 |           48.871 |
| 1800 |               1.995 |                2.993 |           65.332 |
| 2000 |               1.994 |                3.990 |           81.292 |

This is for sorted input list:

|    n |   qsort-fixed-pivot |   qsort-random-pivot |   selection_sort |
|------|---------------------|----------------------|------------------|
|  200 |               1.996 |                0.000 |            0.997 |
|  400 |               5.984 |                0.000 |            2.993 |
|  600 |              14.959 |                0.998 |            6.981 |
|  800 |              25.930 |                0.997 |           11.968 |
| 1000 |              35.904 |                1.994 |           18.949 |
| 1200 |              60.347 |                1.995 |           29.920 |
| 1400 |              69.813 |                1.994 |           37.899 |
| 1600 |              94.747 |                1.994 |           50.864 |
| 1800 |             118.709 |                2.998 |           69.781 |
| 2000 |             172.607 |                2.991 |           77.791 |

For random input, quicksort with fixed pivot and with random pivot have an average time complexity of `O(nlogn)` while selection sort has a time complexity of `O(n^2)`. The running times are within the expected bounds as quick sort algorithms have an average time complexity of `O(nlogn)` and selection sort has a time complexity of `O(n^2)`.

When input changed to the sorted list. Selection sort's performance and quick sort with random pivot keeps the same. However, quick sort with fixed pivot has a time conplexity of `O(n^2)`, this is because it falls into the worst case.



- **1c.**

|      n |   qsort-fixed-pivot |   qsort-random-pivot |   tim_sort |
|--------|---------------------|----------------------|------------|
|  10000 |              12.965 |               18.950 |      0.997 |
|  20000 |              27.925 |               40.461 |      2.992 |
|  30000 |              46.875 |               60.537 |      4.986 |
|  40000 |              63.912 |               96.298 |      5.983 |
|  50000 |              97.738 |              111.702 |      5.983 |
|  60000 |              98.740 |              126.169 |      8.976 |
|  70000 |             115.704 |              152.580 |     10.970 |
|  80000 |             139.626 |              166.556 |     11.968 |
|  90000 |             145.614 |              205.038 |     14.960 |
| 100000 |             170.543 |              217.420 |     14.960 |