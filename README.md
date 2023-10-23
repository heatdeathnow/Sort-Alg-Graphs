## Sorting algorithms currently implemented:
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort

### Languages
In this project, I aim to implement sorting algorithms I'm interested in in Python, Cython and C#. I don't know how to plot graphs for C# yet, as I am a novice. After I have data for all these languages for several sorting algorithms and I have learnt more C#, I will plot graphs comparing their performances.

### Other stuff
The `data_manager` module is responsible for adding new data to the `.csv` files, retrieving data from the `.csv` files and manipulating this data. It can currently take the mean of all columns in order to generated points to be plotted in a graph, and also purge the data of all outliers within a specified _z score_.

The `data_miner` module is responsible for running the sorting algorithms and collecting the performance data and then invoking a `DataManager` object to store it.

The `graph_maker` module is yet very simple and is responsible for plotting the graphs.

##### To be done
- Implement Merge Sort in C#.
- Implement Merge Sort with concurrent recursion.
- Implement other sorting algorithms.
- Refactor the `DataManager` object, seeing as it is unwieldy.
- Add more features to the graphs
