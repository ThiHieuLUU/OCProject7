#! /usr/bin/venv python3
# coding: utf-8

"""In this module, dynamic programming algorithm is implemented to solve the problem of buying
shares. """

import time

from data_treatement import save_solution_to_file


def dynamic_programming(list_of_shares, total_cost_max):
    """This method is applied when total_cost_max and cost of each share are integer.

    The optimal solution is calculated from the solution of the sub-problems.

    Denote B[n][M] the maximum profit obtained when selecting in all n shares with the cost max M.
    Two possibilities:
    - If B[n][M] = B[n – 1][M] then share n is not selected and must find the solution of the
    sub-problem B[n – 1][M].
    - If B[n][M] ≠ B[n – 1][M] then share n is selected and must find the solution of the
    sub-problem B[n – 1][M – C[n]].
    where C[n] is the cost of n-th share.

    - The recursive formula as follows:
        B[i][j]= max(B[i – 1][j], V[i] + B[i – 1][j – C[i]])

    (B[i][j] is the optimal profit with i shares and total_cost_max = j, which is solved
    by solving two sub-problems:
    - finding the optimal profit from (i - 1) shares and total_cost_max = j => appears B[i – 1][j]
    - finding the optimal profit from (i - 1) shares and total_cost_max = j - C[i]
        => appears B[i – 1][j – C[i]]
    )
    """

    start = time.perf_counter()  # To measure time calculating
    matrix = [[0 for x in range(total_cost_max + 1)] for x in range(len(list_of_shares) + 1)]

    # Build the matrix where each element is the optimal profit of a sub-problem.
    for i in range(1, len(list_of_shares) + 1):
        for j in range(1, total_cost_max + 1):
            if list_of_shares[i - 1][1] <= j:
                share_cost = list_of_shares[i - 1][1]
                share_profit = list_of_shares[i - 1][2]
                matrix[i][j] = max(
                    share_profit + matrix[i - 1][j - share_cost],
                    matrix[i - 1][j]
                )
            else:
                matrix[i][j] = matrix[i - 1][j]

    j = total_cost_max
    n = len(list_of_shares)
    selection = []

    # Trace the solution from the last element of matrix
    while j >= 0 and n >= 0:
        share = list_of_shares[n - 1]
        share_cost = share[1]
        share_profit = share[2]
        if matrix[n][j] == matrix[n - 1][j - share_cost] + share_profit:
            selection.append(share)
            j -= share_cost

        n -= 1
    # total_profit = matrix[-1][-1]
    end = time.perf_counter()  # To measure time calculating
    print(f'Dynamic programming takes {end - start} seconds')
    return selection


def dynamic_programming_for_20_shares():
    """Solve problem with 20 shares."""

    total_cost_max = 500
    share_file = input("Please enter file name (input/20_shares.txt or input/20_shares.csv): ")
    method = dynamic_programming
    save_solution_to_file(share_file, total_cost_max, method)


def dynamic_programming_for_dataset_testing():
    """Solve problem with shares in dataset after cleaning."""

    total_cost_max = 500 * 100  # To transform cost from euro to cents.
    share_file = input(
        "Please enter file name (input/dataset1_Python+P7_cleaned.csv or "
        "input/dataset2_Python+P7_cleaned.csv): "
    )
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
        raise "The dataset is not in the list proposed!"
