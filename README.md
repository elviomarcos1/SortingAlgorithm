📊 Comparison of Sorting Algorithms
This project was developed to compare the efficiency of three sorting algorithms: Heap Sort, Selection Sort, and Insertion Sort. The comparison is based on executing these algorithms over randomly generated datasets of varying sizes. For visualizing the results, we use interactive graphs created with the help of the Dash, Plotly, and Pandas libraries.

🧩 Project Description
The main goal of this project is to analyze and compare the performance of the sorting algorithms mentioned above. To achieve this, we followed these steps:

1. Random Data Generation

Created a script that generates random datasets.

Dataset sizes vary from 200 to 5000, in increments of 200.

2. Sorting Algorithms

Heap Sort: An efficient algorithm based on heap data structures.

Selection Sort: A simple sorting algorithm based on selection.

Insertion Sort: An insertion-based sorting algorithm, generally efficient for small datasets.

3. Algorithm Execution

Each algorithm is run on progressively larger random datasets, starting from 200 up to 5000 elements.

We measure the execution time of each algorithm for each dataset size.

4. Results Visualization

We use Dash, Plotly, and Pandas to organize the collected data and create interactive charts.

The charts are displayed on a semi-logarithmic scale, which facilitates comparison of algorithm performance.
