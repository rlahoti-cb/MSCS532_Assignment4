
## Part 1 Heapsort vs Mergesort vs Quicksort on Varying Data Sizes and Types

In this experiment we will be running the heapsort algorithm on varying data sizes (100000, 1000000 elements) and varying data types (sorted, random, reversed sorted).


In order to run the code to analyze heapsort performance, you can run:

```
python3 assignment_4_part_1.py
```

This will output the results to your terminal. I have captured my results to the `results_part_1.txt` file for the run that I am using in my analysis.

I have used the implementation from assignment 2 to capture data for the mergesort and quicksort algorithm on the same sizes of data and the same types of data. This data is also captured in the `results_part_1.txt` file.

## Part 2 Priority Queue Task Simulation

In this experiment, we will be running a task simulation using a priority queue as the underlying data structure. We will analyze the time complexity of the insert, extract, and increase_key operations for the task simulator. We will run the operations against an input of 100K and 1M tasks. This will allow us to compare the performance of the three operations as the input data increases to see if there are any differences between the theoretical expectations and emperical results.

In order to run the code to generate the data, you can run:

```
python3 assignmnet_4_part_2.py
```

This will output the results to your terminal. I have captured my results to the `results_part_2.txt` file for hte run that I am using in my analysis.
