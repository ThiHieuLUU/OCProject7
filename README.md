## About the project
This project aims to use different algorithms (brute force, dynamic programming, greedy) in order to 
solve the problem of buying shares. The problem here is to maximize the profit of the purchased shares
such that the total cost does not exceed a given amount.

## About the main structure 
```
OCProject7/
   ├── algorithm_code/
   │   ├── input/
   │   ├── output/
   │   ├── data_cleanning.py
   │   ├── data_treatement.py
   │   ├── bruteforce.py
   │   ├── optimized.py
   │   ├── greedy.py
   ├── slides/  
   │   ├── slides_p7.pdf  
   │   ├── exploration_donnees.xlsx
   ├── README.md
   ├── requirements.txt

```
About some directories: 
- `input` contains the datasets for testing different algorithms.
- `output` contains results saved under text file format. In these files, information about
the list of shares to buy, the total cost, the total profit for each algorithm is shown.
- `slides` contains slides for explications of these algorithms. `exploration_donnees.xlsx` contains 
the dataset (before and after cleaning) and the comparison for different decisions.

About some files: 
- `data_cleanning.py` is used to clean data (remove shares with name duplicated, remove shares with negative price or nagative profit).
`data_cleanning.py` is launched to clean the files: `dataset1_Python+P7.csv` and `dataset2_Python+P7.csv`. 
The cleaned data then used as input for testing of different algorithms.
## Process  
1. Clone and launch the project:
   ```
   git clone  https://github.com/ThiHieuLUU/OCProject7.git
   cd OCProject7/
   
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt 
   ```   
   If in `input` directory, there are no cleaned data yet or you want to re-clean data, launch `python data_cleanning.py` first.
2. Solve the problem of buying shares with different methods

    Go to the directory "algorithm_code"

    2.1. Bruteforce  
    ```
    python bruteforce.py
    ```
   Then select the data file proposed (text or csv) to run the algorithm.

    2.2. Dynamic programming
    ```
    python optimized.py
    ```
   Then select the data file among different datasets proposed (20 actions / dataset1 / dataset2) to run the algorithm.

    2.2. Greedy
    ```
    python greedy.py
    ```
   Then select the data file among different datasets proposed (20 actions / dataset1 / dataset2) to run the algorithm.

3. Results

   See in the directory "output"
## Check code with flake8
From the `OCProject7` directory, run `flake8`.