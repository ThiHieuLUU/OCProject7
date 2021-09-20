"""In this module, dynamic programming  method is implemented to solve problem of buying
shares. """

import time
import os

from data_treatement import save_solution_to_file

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def dynamic_programming(list_of_shares, total_cost_max):
    """This method is applied when total_cost_max and cost of each share are integer.

    The optimal solution is calculated on the resolution of sub-problems.

    Denote B[n][M] the maximum profit obtained when selecting in all n shares with the cost max M.
    Two possibilities:
    - If B[n][M] = B[n – 1][M] then share n is not selected and must find the solution of
    sub-problem B[n – 1][M].
    - If B[n][M] ≠ B[n – 1][M] then share n is selected n and must find the solution of
    sub-problem B[n – 1][M – W[n]].
    where W[n] is the cost of n-th share.

    - The recursive formula as follows:
        B[i][j]= max(B[i – 1][j], V[i]+B[i – 1][j – W[i]])
    (Problem with i shares and total_cost_max = j is solved by 2 sub-problems:
    - problem with (i - 1) shares and total_cost_max = j
    - problem with (i - 1) shares and total_cost_max = j - W[i]
    )
    """
    start = time.perf_counter()
    matrix = [[0 for x in range(total_cost_max + 1)] for x in range(len(list_of_shares) + 1)]

    for i in range(1, len(list_of_shares) + 1):
        for w in range(1, total_cost_max + 1):
            if list_of_shares[i - 1][1] <= w:
                share_cost = list_of_shares[i - 1][1]
                share_profit = list_of_shares[i - 1][2]
                matrix[i][w] = max(
                    share_profit + matrix[i - 1][w - share_cost],
                    matrix[i - 1][w]
                )
            else:
                matrix[i][w] = matrix[i - 1][w]

    w = total_cost_max
    n = len(list_of_shares)
    selection = []

    while w >= 0 and n >= 0:
        share = list_of_shares[n - 1]
        share_cost = share[1]
        share_profit = share[2]
        if matrix[n][w] == matrix[n - 1][w - share_cost] + share_profit:
            selection.append(share)
            w -= share_cost

        n -= 1
    # total_profit = matrix[-1][-1]
    end = time.perf_counter()
    print(f'Dynamic programming takes {end - start} seconds')
    return selection


def dynamic_programming_for_20_shares():
    """Solve problem with 20 shares."""

    total_cost_max = 500
    share_file = input("Please enter file name (/input/20_shares.txt or /input/20_shares.csv): ")
    share_file = SCRIPT_DIR + share_file
    method = dynamic_programming
    save_solution_to_file(share_file, total_cost_max, method)


def dynamic_programming_for_dataset_testing():
    """Solve problem with shares in dataset after cleaning."""

    total_cost_max = 500 * 100
    share_file = input(
        "Please enter file name (/input/dataset1_Python+P7_cleaned.csv or "
        "/input/dataset2_Python+P7_cleaned.csv): "
    )

    share_file = SCRIPT_DIR + share_file
    method = dynamic_programming
    save_solution_to_file(share_file, total_cost_max, method)


if __name__ == '__main__':
    which_dataset = int(input("Select dataset: 1 - for 20 shares, 2 - for Sienna's dataset: "))

    # Following the choice of dataset, the corresponding solution will be given.
    if which_dataset == 1:
        dynamic_programming_for_20_shares()
    elif which_dataset == 2:
        dynamic_programming_for_dataset_testing()
    else:
        raise "Select is not compatible."
