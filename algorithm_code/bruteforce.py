"""In this module, brute force method is implemented to solve problem of actions."""

import csv


def read_text_file(file_name):
    """Read a text file about actions' information. The format of the file:

    Column1: action's name
    Column2: cost of an action (in euro)
    Column3: profit of an action after 2 years (in percentage)

    After reading, return information under a list of tuple like below:
    [("Action-1", 20, 1), ("Action-2", 30, 3), ...]
    Here:
     - cost of an action is transformed from string to int 
     - profit of an action is calculated by multiplying action cost with action profit value
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


def read_csv_file(file_name):
    """Read a csv file about actions' information. The format of the file:

    Column1: action's name
    Column2: cost of an action (in euro)
    Column3: profit of an action after 2 years (in percentage)

    After reading, return information under a list of tuple like below:
    [("Action-1", 20, 1), ("Action-2", 30, 3), ...]
    Here:
     - cost of an action is transformed from string to int 
     - profit of an action is calculated by multiplying action cost with action profit value
    """

    percentage_str = "%"
    percentage_value = 0.01

    with open(file_name, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        actions = list(reader)

    for action in actions:
        action['profit'] = float(action['profit'].replace(percentage_str, ''))
        action['price'] = int(action['price'])

    list_of_actions = [
        (action['name'], action['price'], action['price'] * action['profit'] * percentage_value)
        for action in actions
    ]

    return list_of_actions


def get_total_profit(selection):
    """Get total profit of actions from a selection of actions. """

    return sum([action[2] for action in selection])


def get_total_cost(selection):
    """Get total cost of actions from a selection of actions. """

    return sum([action[1] for action in selection])


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


def save_file(file_name_to_save, solution):
    """Save solution to a file."""

    with open(file_name_to_save, 'w') as file:
        file.write('name, price, profit \n')
        for action in solution:
            file.write(f'{str(action)}\n')

        file.write('\n')
        file.write(f'Total cost: {get_total_cost(solution)}\n')
        file.write(f'Total profit: {get_total_profit(solution)}\n')


def get_solution(action_file, total_cost_max):
    """Get solution from brute force method."""

    if ".txt" in action_file:
        actions = read_text_file(action_file)
    elif ".csv" in action_file:
        actions = read_csv_file(action_file)
    else:
        raise "File not found."

    solution = brute_force(actions, total_cost_max)

    # Create a file name to save output from the input file name.
    file_name_to_save = action_file.split(".")[0].replace("input/", "output/") + "_brute_force.txt"
    save_file(file_name_to_save, solution)
    print(f'See the result in the file: {file_name_to_save}')


if __name__ == '__main__':
    total_cost_max = 500
    action_file = input("Please enter file name (input/20_actions.txt or input/20_actions.csv): ")

    get_solution(action_file, total_cost_max)
