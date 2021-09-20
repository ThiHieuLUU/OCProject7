"""In this module, greedy method is implemented to solve problem of buying shares. """

import os
import time

from data_treatement import save_solution_to_file

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def sort_shares(list_of_shares):
    """Sort on the efficiency of profit in descending order."""

    return sorted(list_of_shares,
                  key=lambda list_of_shares: list_of_shares[2] / list_of_shares[1],
                  reverse=True)


def greedy(list_of_shares, total_cost_max):
    """An approximate method to find a solution close the optimal solution.

    This method can be applied with total_cost_max and cost of each share are float.

    The efficiency (here, the efficiency is the profit, because the profit is represented
    in percentage) is sorted in descending order and added in the solution in function of
    the cost reminder.
    """
    start = time.perf_counter()
    list_of_shares_sorted = sort_shares(list_of_shares)
    total_cost = 0
    total_profit = 0
    index = 0
    shares_len = len(list_of_shares_sorted)
    selection = []
    while total_cost <= total_cost_max and index < shares_len:
        rest = total_cost_max - total_cost
        share = list_of_shares_sorted[index]
        share_cost = share[1]
        share_profit = share[2]
        if share_cost <= rest:
            selection.append(share)
            total_cost = total_cost + share_cost
            total_profit = total_profit + share_profit
        index = index + 1

    end = time.perf_counter()
    print(f'Greedy takes {end - start} seconds')
    return selection


def greedy_for_20_shares():
    """Solve problem with 20 shares."""

    total_cost_max = 500
    share_file = input(
        "Please enter file name (/input/20_shares.txt or /input/20_shares.csv): ")
    share_file = SCRIPT_DIR + share_file
    method = greedy
    save_solution_to_file(share_file, total_cost_max, method)


def greedy_for_dataset_testing():
    """Solve problem with shares in dataset after cleaning."""

    total_cost_max = 500 * 100
    share_file = input(
        "Please enter file name (/input/dataset1_Python+P7_cleaned.csv or "
        "/input/dataset2_Python+P7_cleaned.csv): "
    )

    share_file = SCRIPT_DIR + share_file
    method = greedy
    save_solution_to_file(share_file, total_cost_max, method)


if __name__ == '__main__':
    which_dataset = int(input("Select dataset: 1 - for 20 shares, 2 - for Sienna's dataset: "))

    # Following the choice of dataset, the corresponding solution will be given.
    if which_dataset == 1:
        greedy_for_20_shares()
    elif which_dataset == 2:
        greedy_for_dataset_testing()
    else:
        raise "Select is not compatible."
