import shutil
from ConstDefinit import (
    TIME_FRAME,
    COLUMN_MAPPING
) 

def table_header_rename(file_data):
    print(f"[{TIME_FRAME}] table_header_rename(): Start")
    file_data.rename(columns=COLUMN_MAPPING, inplace=True)

def data_validation(file_data):
    print(f"[{TIME_FRAME}] data_validation(): Start")
    file_data = file_data.dropna(axis=0, how='any')
    table_header_rename(file_data)

    # 剔除 pH 值不在 2.9 到 3.9 范围内的数据
    ph_column_name = COLUMN_MAPPING['pH']
    file_data = file_data[(file_data[ph_column_name] >= 2.9) & (file_data[ph_column_name] <= 3.9)]

     # 剔除数据中存在负数的行
    file_data = file_data[(file_data >= 0).all(axis=1)]

    # 剔除质量属性列中数据不在 1~10 区间内的行
    quality_column_name = COLUMN_MAPPING['quality']
    file_data = file_data[(file_data[quality_column_name] >= 1) & (file_data[quality_column_name] <= 10)]

    # print(f"[{TIME_FRAME}] dataset_preparation(): check first five lines")
    # print(file_data.head())
    print(f"[{TIME_FRAME}] data_validation(): End")
    return file_data

def remove_outliers(file_data):
    # 获取数据的统计描述
    stats = file_data.describe()

    # 获取Q1和Q3的值
    Q1 = stats.loc['25%']
    Q3 = stats.loc['75%']

    # 计算IQR（四分位距）
    IQR = Q3 - Q1

    # 定义异常值的范围
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # 去除异常值
    cleaned_data = file_data[~((file_data < lower_bound) | (file_data > upper_bound)).any(axis=1)]

    return cleaned_data

def data_cleanUp(file_data):
    print(f"[{TIME_FRAME}] data_clean(): Start")
    num_data_entries_before_filter = len(file_data)
    new_file_data = remove_outliers(file_data)
    num_data_entries_after_filter = len(new_file_data)
    print(f"[{TIME_FRAME}] dataMining(): number of data entries that has been removed is: {num_data_entries_before_filter - num_data_entries_after_filter}")
    return new_file_data

import os
from DataDownload import dataset_preparation
from DataCleanUp import data_cleanUp, data_validation
from DataVisualization import build_Histograms_and_BoxPlots, data_feature_anlysis, key_feature_analysis
from ConstDefinit import (
    TIME_FRAME
)

def clear_visualization_results():
    output_directory = 'visualizationResult'
    for filename in os.listdir(output_directory):
        file_path = os.path.join(output_directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')