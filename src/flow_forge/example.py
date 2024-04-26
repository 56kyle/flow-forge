import pandas as pd

from flow_forge.data_endpoint.file import FileDataEndpoint
from flow_forge.extractor.file_to_pd_data_frame import CsvFileToPdDataFrameExtractor


if __name__ == '__main__':
    csv_file_to_pd_data_frame_extractor: CsvFileToPdDataFrameExtractor = CsvFileToPdDataFrameExtractor()
    df: pd.DataFrame = csv_file_to_pd_data_frame_extractor(
        FileDataEndpoint("https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv")
    )
    print(df)

