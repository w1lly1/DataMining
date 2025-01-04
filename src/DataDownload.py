import kagglehub
import pandas as pd
import os
from ConstDefinit import (
    TIME_FRAME,
    KAGGLE_DATASET_DOWNLOAD_PATH,
    KAGGLE_DATASET_FILE_NAME
)

def download_dataset():
    path = kagglehub.dataset_download(KAGGLE_DATASET_DOWNLOAD_PATH)
    print(f"[{TIME_FRAME}] download_dataset(): path {path}")
    return path


def dataset_preparation():
    dataset_path = download_dataset()
    file_data_path = os.path.join(dataset_path, KAGGLE_DATASET_FILE_NAME)

    if not os.path.exists(file_data_path):
        raise FileNotFoundError(f"[{TIME_FRAME}] dataset_preparation(): File not found at {file_data_path}")
    else:
        print(f"[{TIME_FRAME}] dataset_preparation(): File found at {file_data_path}")

    try:
        file_data = pd.read_csv(file_data_path, encoding='latin-1')
        print(f"[{TIME_FRAME}] dataset_preparation(): check first five lines")
        print(file_data.head())
        return file_data
    except Exception as e:
        print(f"[{TIME_FRAME}] dataset_preparation(): Error reading CSV file: {e}")
        raise e