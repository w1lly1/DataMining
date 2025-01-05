from DataDownload import dataset_preparation
from DataCleanUp import data_cleanUp, data_validation, clear_visualization_results
from DataVisualization import build_Histograms_and_BoxPlots, data_feature_anlysis, key_feature_analysis
from DataPrediction import data_prediction
from ConstDefinit import (
    TIME_FRAME
)

def dataMining():
    print(f"[{TIME_FRAME}] dataMining(): Start")
    print(f"[{TIME_FRAME}] dataMining(): start files clean up")
    clear_visualization_results()

    print(f"[{TIME_FRAME}] dataMining(): start dataset preparation")
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

    print(f"[{TIME_FRAME}] dataMining(): start feature analysis")
    file_data = data_feature_anlysis(file_data)

    print(f"[{TIME_FRAME}] dataMining(): start key feature analysis")
    # 对具有明显正线性相关性的参数包括固定酸度，柠檬酸，硫酸盐，
    # 和负线性相关的参数挥发性酸度做多变量分析
    key_feature_analysis(file_data)

    print(f"[{TIME_FRAME}] dataMining(): start data prediction")
    data_prediction(file_data)


    print(f"[{TIME_FRAME}] dataMining(): End")

if __name__ == "__main__":
    dataMining()
