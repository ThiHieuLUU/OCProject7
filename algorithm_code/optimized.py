"""In this module, dynamic programming  method is implemented to solve problem of buying
actions. """

import os

from algorithm_code.data_treatement import save_solution_to_file

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def dynamic_programming(list_of_actions, total_cost_max):
    """This method is applied when total_cost_max and cost of each action are integer.

    The optimal solution is calculated on the resolution of sub-problems.

    Denote B[n][M] the maximum profit obtained when selecting in all n actions with the cost limit M.
    Two possibilities:
    - If B[n][M] = B[n – 1][M] then action n is not selected and must find the solution of sub-problem B[n – 1][M].
    - If B[n][M] ≠ B[n – 1][M] then action n is selected n and must find the solution of sub-problem B[n – 1][M – W[n]].
    where W[n] is the cost of n-th action.

    - The recursive formula as follows:
        B[i][j]= max(B[i – 1][j], V[i]+B[i – 1][j – W[i]])
    (Problem with i actions and total_cost_max = j is solved by 2 sub-problems:
    - problem with (i - 1) actions and total_cost_max = j
    - problem with (i - 1) actions and total_cost_max = j - W[i]
    )
    """

    matrix = [[0 for x in range(total_cost_max + 1)] for x in range(len(list_of_actions) + 1)]

    for i in range(1, len(list_of_actions) + 1):
        for w in range(1, total_cost_max + 1):
            if list_of_actions[i - 1][1] <= w:
                action_cost = list_of_actions[i - 1][1]
                action_profit = list_of_actions[i - 1][2]
                matrix[i][w] = max(
                    action_profit + matrix[i - 1][w - action_cost],
                    matrix[i - 1][w]
                )
            else:
                matrix[i][w] = matrix[i - 1][w]

    w = total_cost_max
    n = len(list_of_actions)
    selection = []

    while w >= 0 and n >= 0:
        action = list_of_actions[n - 1]
        action_cost = action[1]
        action_profit = action[2]
        if matrix[n][w] == matrix[n - 1][w - action_cost] + action_profit:
            selection.append(action)
            w -= action_cost

        n -= 1
    # total_profit = matrix[-1][-1]
    return selection


def dynamic_programming_for_20_actions():
    """Solve problem with 20 actions."""

    total_cost_max = 500
    action_file = input("Please enter file name (/input/20_actions.txt or /input/20_actions.csv): ")
    action_file = SCRIPT_DIR + action_file
    method = dynamic_programming
    save_solution_to_file(action_file, total_cost_max, method)


def dynamic_programming_for_dataset_testing():
    """Solve problem with actions in dataset after cleaning."""

    total_cost_max = 500 * 100
    action_file = input(
        "Please enter file name (/input/dataset1_Python+P7_cleaned.csv or "
        "/input/dataset2_Python+P7_cleaned.csv): "
    )

    action_file = SCRIPT_DIR + action_file
    method = dynamic_programming
    save_solution_to_file(action_file, total_cost_max, method)


if __name__ == '__main__':
    which_dataset = int(input("Select dataset: 1 - for 20 actions, 2 - for Sienna's data set: "))

    # Following the choice of dataset, the corresponding solution will be given.
    if which_dataset == 1:
        dynamic_programming_for_20_actions()
    elif which_dataset == 2:
        dynamic_programming_for_dataset_testing()
    else:
        raise "Select is not compatible."
