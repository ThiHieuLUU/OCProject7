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
        line[1] = float(line[1])

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


def force_brute(list_of_actions, total_cost_max):
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


if __name__ == '__main__':
    actions = read_file('20_actions.txt')
    sol = force_brute(actions, 500)
    print(f'solution: {sol}')
    print(f'Total cost: {get_total_cost(sol)}')
    print(f'Total profit: {get_total_profit(sol)}')
