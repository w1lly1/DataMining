from DataDownload import dataset_preparation
from DataCleanUp import data_cleanUp, data_validation
from DataVisualization import build_Histograms_and_BoxPlots
from DataFeatureAnalysis import data_feature_anlysis
from ConstDefinit import (
    TIME_FRAME
)

def dataMining():
    print(f"[{TIME_FRAME}] dataMining(): Start")
    print(f"[{TIME_FRAME}] dataMining(): start dataset preparation done")
    file_data = dataset_preparation()
    # print(f"[{TIME_FRAME}] dataMining(): check first five lines")
    # print(file_data.head())

    print(f"[{TIME_FRAME}] dataMining(): start dataset validation")
    file_data = data_validation(file_data)

    print(f"[{TIME_FRAME}] dataMining(): build Histograms&BoxPlots")
    build_Histograms_and_BoxPlots(file_data, "before_cleanUp")

    print(f"[{TIME_FRAME}] dataMining(): start dataset cleanUp")
    file_data = data_cleanUp(file_data)

    print(f"[{TIME_FRAME}] dataMining(): build Histograms&BoxPlots")
    build_Histograms_and_BoxPlots(file_data, "after_cleanUp")

    print(f"[{TIME_FRAME}] dataMining(): feature analysis")
    file_data = data_feature_anlysis(file_data)

    print(f"[{TIME_FRAME}] dataMining(): End")

if __name__ == "__main__":
    dataMining()
