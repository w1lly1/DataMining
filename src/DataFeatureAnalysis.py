import os
import numpy as np
import matplotlib.pyplot as plt
from DataVisualization import feature_influence_to_quality_visualize
from ConstDefinit import (
    TIME_FRAME,

) 

def feature_influence_to_quality_analysis(file_data):
    feature_influence_to_quality_visualize(file_data, "feature_influence_to_quality")

def multi_feature_analysis(file_data):
    print(f"[{TIME_FRAME}] multi_feature_analysis(): Start")
    print(f"[{TIME_FRAME}] multi_feature_analysis(): End")

def data_feature_anlysis(file_data):
    print(f"[{TIME_FRAME}] data_anlysis(): Start")

    feature_influence_to_quality_analysis(file_data)

    multi_feature_analysis(file_data)

    print(f"[{TIME_FRAME}] data_anlysis(): End")
    return file_data