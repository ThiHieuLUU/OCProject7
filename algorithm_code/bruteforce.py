#! /usr/bin/venv python3
# coding: utf-8

"""In this module, brute force algorithm is implemented to solve problem of buying shares."""

import time

from data_treatement import (
    get_total_profit,
    get_total_cost,
    save_solution_to_file
)


def brute_force(list_of_shares, total_cost_max):
    """Generate all combinations of shares.

    For each combination, calculate the total cost and the total profit to take the best solution
    under the constraint: maximize the profit while the total cost doesn't exceed a given value.
    """
    start = time.perf_counter()  # To measure time calculating

    nbr_of_share_types = len(list_of_shares)
    nbr_of_combinations = 2 ** nbr_of_share_types
    solution = []

    for key in range(nbr_of_combinations):
        choice = bin(key)[2:]
        len_choice = len(choice)

        # Each share choice must be represented in a combination either by 0 (not selected) or
        # by 1 (selected)
        if len_choice < nbr_of_share_types:
            choice = (nbr_of_share_types - len_choice) * '0' + choice
        # Until here, len(choice) = nbr_of_share_types

        combination = []
        for i in range(nbr_of_share_types):
            if choice[i] == '1':
                combination.append(list_of_shares[i])

        if get_total_profit(combination) > get_total_profit(solution):
            if get_total_cost(combination) <= total_cost_max:
                solution = combination

    end = time.perf_counter()  # To measure time calculating
    print(f'Brute force takes {end - start} seconds')
    return solution


def brute_force_for_20_shares():
    """Solve problem with 20 shares."""

    total_cost_max = 500
    share_file = input("Please enter file name (input/20_shares.txt or input/20_shares.csv): ")
    method = brute_force
    save_solution_to_file(share_file, total_cost_max, method)


# def brute_force_for_test_dataset():
#     """Solve problem with shares in dataset after cleaning.
#     It will take a huge time, don't run this.
#     """
#     total_cost_max = 500
#     share_file = input("Please enter file name (input/dataset1_Python+P7_cleaned.csv or "
#                        "input/dataset2_Python+P7_cleaned.csv): ")
#     method = brute_force
#     save_solution_to_file(share_file, total_cost_max, method)


if __name__ == '__main__':
    brute_force_for_20_shares()
