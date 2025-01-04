from DataDownload import dataset_preparation
from DataCleanUp import data_cleanUp
from DataVisualization import data_visualize
from ConstDefinit import (
    TIME_FRAME
)

def dataMining():
    print(f"[{TIME_FRAME}] dataMining(): Start")
    file_data = dataset_preparation()
    print(f"[{TIME_FRAME}] dataMining(): dataset preparation done")
    data_cleanUp(file_data)
    print(f"[{TIME_FRAME}] dataMining(): dataset cleanUp done")
    data_visualize(file_data)
    print(f"[{TIME_FRAME}] dataMining(): dataset visualize done")
    print(f"[{TIME_FRAME}] dataMining(): End")

if __name__ == "__main__":
    dataMining()
