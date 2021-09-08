def read_file(file_name):
    """Read a text file about actions' information. The format of the file:

    Column1: action's name
    Column2: cost of an action (in euro)
    Column3: profit of an action after 2 years (in percentage)

    After reading, return information under a list of tuple like below:
    [("Action-1", 20, 1), ("Action-2", 30, 3)]
    """

    percentage_str = "%"
    percentage_value = 0.01

    with open(file_name) as f:
        lines = f.read().splitlines()
    # Eliminate the first line - header line
    lines = lines[1:]
    # Eliminate the percentage sign then split by tab "\t"
    lines = [line.replace(percentage_str, '').split('\t') for line in lines]

    for line in lines:
        # Transform cost from string to float
        line[1] = int(line[1])

        # Replace percentage in each line[2] by the real profit (after 2 years)
        # First, transform percentage to value, for exemple: 5% becomes 5*0.01 = 0.05
        line[2] = float(line[2]) * percentage_value
        # Then calculate the real profit
        # For exemple, an action costs 20 euros with profit 5% so the total profil is 20 * 0.05
        line[2] = line[1] * line[2]
    lines = [tuple(line) for line in lines]
    return lines


def get_total_profit(selection):
    """Get total profit of actions from a selection of actions. """

    return sum([item[2] for item in selection])


def get_total_cost(selection):
    """Get total cost of actions from a selection of actions. """

    return sum([item[1] for item in selection])


def brute_force(list_of_actions, total_cost_max):
    """Generate all combinations of actions.

    For each combination, calculate the total cost and the total profit to take the best solution
    under the constraint: maximize the profit while the cost doesn't exceed a given value.
    """

    nbr_of_action_types = len(list_of_actions)
    nbr_of_combinations = 2 ** nbr_of_action_types
    solution = []

    for key in range(nbr_of_combinations):
        choice = bin(key)[2:]
        len_choice = len(choice)

        # Each action choice must be represented in a combination either by 0 (not selected) or
        # by 1 (selected)
        if len_choice < nbr_of_action_types:
            choice = (nbr_of_action_types - len_choice) * '0' + choice
        # Until here, len(choice) = nbr_of_action_types

        combination = []
        for i in range(nbr_of_action_types):
            if choice[i] == '1':
                combination.append(list_of_actions[i])

        if get_total_profit(combination) > get_total_profit(solution):
            if get_total_cost(combination) <= total_cost_max:
                solution = combination
    return solution


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
    total_profit = matrix[-1][-1]
    return total_profit, selection


def sort_actions(list_of_actions):
    """Sort on the efficiency of profit in descending order."""

    return sorted(list_of_actions, key=lambda list_of_actions: list_of_actions[2]/list_of_actions[1], reverse=True)


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
    return total_profit, selection


if __name__ == '__main__':
    total_cost_max = 500
    list_of_actions = read_file('20_actions.txt')
    print("*" * 10)

    sol = brute_force(list_of_actions, total_cost_max)
    print(f'Brute force solution: {sol}')
    print(f'Total cost: {get_total_cost(sol)}')
    print(f'Total profit: {get_total_profit(sol)}')

    print("*" * 10)
    profit, sol = dynamic_programming(list_of_actions, total_cost_max)
    print(f'Dynamic programming solution: {sol}')
    print(f'Total cost: {get_total_cost(sol)}')
    print(f'Total profit: {get_total_profit(sol)}')
    print(f'Total profit via matrix: {profit}')

    print("*" * 10)
    profit, sol = greedy(list_of_actions, total_cost_max)
    print(f'Greedy solution: {sol}')
    print(f'Total cost: {get_total_cost(sol)}')
    print(f'Total profit: {get_total_profit(sol)}')
    print(f'Total profit via greedy function: {profit}')