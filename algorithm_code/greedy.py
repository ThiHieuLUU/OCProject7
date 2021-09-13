"""In this module, greedy method is implemented to solve problem of buying actions. """

from info_treatement import save_solution_to_file



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
    return selection


if __name__ == '__main__':
    total_cost_max = 500
    action_file = input("Please enter file name (input/20_actions.txt or input/20_actions.csv): ")
    method = greedy
    save_solution_to_file(action_file, total_cost_max, method)
