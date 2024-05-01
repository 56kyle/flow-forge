import fsspec
import pandas as pd


if __name__ == '__main__':
    with fsspec.open("https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv") as file:
        df: pd.DataFrame = pd.read_csv(file)

