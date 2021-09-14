import csv

from os.path import exists as file_exists
import pandas as pd


def clean_data(name_file):
    df = pd.read_csv(name_file)
    df_no_duplicates = df.drop_duplicates(subset=['name'])
    df_positive = df_no_duplicates[
        (df_no_duplicates['price'] > 0) & (df_no_duplicates['profit'] >= 0)]
    # Create a file name to save data cleaned from the input file name
    data_cleaned_csv_file = name_file.split(".")[0] + "_cleaned.csv"

    if not file_exists(data_cleaned_csv_file):
        df_positive.to_csv(data_cleaned_csv_file, index=False)


if __name__ == '__main__':
    for name_file in ["input/dataset1_Python+P7.csv", "input/dataset2_Python+P7.csv"]:
        clean_data(name_file)
