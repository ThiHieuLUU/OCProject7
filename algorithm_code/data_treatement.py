"""In this module, some functionalities used for different algorithms will be implemented,
such as: read data from a file, save data to a file or calculate the total cost, the total profit.
"""

import csv
from os.path import exists as file_exists


def read_text_file(file_name):
    """Read a text file about shares' information. The format of the file:

    Column1: share's name
    Column2: cost of a share (in euro)
    Column3: profit of a share after 2 years (in percentage)

    After reading, return information under a list of tuple like below:
    [("share-1", 20, 1), ("share-2", 30, 3), ...]
    Here:
     - cost of a share is transformed from string to int
     - profit of a share is calculated by multiplying share cost with share profit value
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
        # Transform cost from string to float, if using dymanic_programming, it must be interger
        # line[1] = float(line[1])
        line[1] = int(line[1])

        # Replace percentage in each line[2] by the real profit (after 2 years)
        # First, transform percentage to value, for exemple: 5% becomes 5*0.01 = 0.05
        line[2] = float(line[2]) * percentage_value
        # Then calculate the real profit
        # For exemple, a share costs 20 euros with profit 5% so the total profil is 20 * 0.05
        line[2] = line[1] * line[2]
    lines = [tuple(line) for line in lines]
    return lines


def read_csv_file(file_name):
    """Read a csv file about shares' information. The format of the file:

    Column1: share's name
    Column2: cost of a share (in euro)
    Column3: profit of a share after 2 years (in percentage)

    After reading, return information under a list of tuple like below:
    [("share-1", 20, 1), ("share-2", 30, 3), ...]
    Here:
     - cost of a share is transformed from string to int
     - profit of a share is calculated by multiplying share cost with share profit value
    """

    percentage_str = "%"
    percentage_value = 0.01

    with open(file_name, encoding='utf-8') as csvfile:
        lines = csv.DictReader(csvfile)
        shares = list(lines)

    for share in shares:
        share['profit'] = float(share['profit'].replace(percentage_str, ''))
        share['price'] = int(share['price'])

    list_of_shares = [
        (share['name'], share['price'], share['price'] * share['profit'] * percentage_value)
        for share in shares
    ]

    return list_of_shares


def read_cleaned_dataset(share_file):
    """Read then transform data to ready to use for the resolution of different methods.

    In particular, for dynamic programming method, cost of each share must be an integer.
    Therefore, price must be multiplied with 100 in this case to become an integer.
    """
    if not file_exists(share_file):
        raise f'File not found {share_file}'

    with open(share_file, 'r') as file:
        lines = csv.DictReader(file)
        array = list(lines)

    list_of_shares = [
        (a['name'], int(float(a['price']) * 100), float(a['price']) * float(a['profit'])) for a in
        array]
    return list_of_shares


def get_total_profit(selection):
    """Get total profit of shares from a selection of shares. """

    return sum([share[2] for share in selection])


def get_total_cost(selection):
    """Get total cost of shares from a selection of shares. """

    return sum([share[1] for share in selection])


def save_file(file_name_to_save, solution):
    """Save solution to a file."""

    with open(file_name_to_save, 'w') as file:
        file.write('name, price, profit \n')
        for share in solution:
            file.write(f'{str(share)}\n')

        file.write('\n')
        file.write(f'Total cost: {get_total_cost(solution)}\n')
        file.write(f'Total profit: {get_total_profit(solution)}\n')


def save_solution_to_file(share_file, total_cost_max, method):
    """Save solution to a file."""

    if ".txt" in share_file:
        shares = read_text_file(share_file)
    elif ".csv" in share_file and "20" in share_file:
        shares = read_csv_file(share_file)
    elif "dataset" in share_file:
        print(share_file)
        shares = read_cleaned_dataset(share_file)
    else:
        raise "File not found."

    solution = method(shares, total_cost_max)

    # Create a file name to save output from the input file name and method resolution selected.
    input_name = share_file.split(".")[0]
    output_name = input_name.replace("input/", "output/") + "_" + f'{method.__name__}' + ".txt "

    save_file(output_name, solution)
    print(f'See the result in the file: {output_name}')
