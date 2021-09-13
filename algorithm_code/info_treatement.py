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


def save_file(file_name_to_save, solution):
    """Save solution to a file."""

    with open(file_name_to_save, 'w') as file:
        file.write('name, price, profit \n')
        for action in solution:
            file.write(f'{str(action)}\n')

        file.write('\n')
        file.write(f'Total cost: {get_total_cost(solution)}\n')
        file.write(f'Total profit: {get_total_profit(solution)}\n')


def save_solution_to_file(action_file, total_cost_max, method):
    """Get solution from brute force method."""

    if ".txt" in action_file:
        actions = read_text_file(action_file)
    elif ".csv" in action_file:
        actions = read_csv_file(action_file)
    else:
        raise "File not found."

    solution = method(actions, total_cost_max)

    # Create a file name to save output from the input file name and method resolution selected.
    file_name_to_save = action_file.split(".")[0].replace("input/", "output/") \
                        + "_" + f'{method.__name__}' + ".txt"

    save_file(file_name_to_save, solution)
    print(f'See the result in the file: {file_name_to_save}')
