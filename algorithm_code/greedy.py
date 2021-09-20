"""In this module, greedy method is implemented to solve problem of buying actions. """
import os
import time

from data_treatement import save_solution_to_file

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def sort_actions(list_of_actions):
    """Sort on the efficiency of profit in descending order."""

    return sorted(list_of_actions,
                  key=lambda list_of_actions: list_of_actions[2] / list_of_actions[1],
                  reverse=True)


def greedy(list_of_actions, total_cost_max):
    """An approximate method to find a solution close the optimal solution.

    This method can be applied with total_cost_max and cost of each action are float.
    The profit is sorted in descending order and added in the solution in function of the cost reminder.
    """
    start = time.perf_counter()
    list_of_actions_sorted = sort_actions(list_of_actions)
    total_cost = 0
    total_profit = 0
    index = 0
    actions_len = len(list_of_actions_sorted)
    selection = []
    while total_cost <= total_cost_max and index < actions_len:
        rest = total_cost_max - total_cost
        action = list_of_actions_sorted[index]
        action_cost = action[1]
        action_profit = action[2]
        if action_cost <= rest:
            selection.append(action)
            total_cost = total_cost + action_cost
            total_profit = total_profit + action_profit
        index = index + 1

    end = time.perf_counter()
    print(f'Greedy takes {end - start} seconds')
    return selection


def greedy_for_20_actions():
    """Solve problem with 20 actions."""

    total_cost_max = 500
    action_file = input(
        "Please enter file name (/input/20_actions.txt or /input/20_actions.csv): ")
    action_file = SCRIPT_DIR + action_file
    method = greedy
    save_solution_to_file(action_file, total_cost_max, method)


def greedy_for_dataset_testing():
    """Solve problem with actions in dataset after cleaning."""

    total_cost_max = 500 * 100
    action_file = input(
        "Please enter file name (/input/dataset1_Python+P7_cleaned.csv or "
        "/input/dataset2_Python+P7_cleaned.csv): "
    )

    action_file = SCRIPT_DIR + action_file
    method = greedy
    save_solution_to_file(action_file, total_cost_max, method)


if __name__ == '__main__':
    which_dataset = int(input("Select dataset: 1 - for 20 actions, 2 - for Sienna's data set: "))

    # Following the choice of dataset, the corresponding solution will be given.
    if which_dataset == 1:
        greedy_for_20_actions()
    elif which_dataset == 2:
        greedy_for_dataset_testing()
    else:
        raise "Select is not compatible."

