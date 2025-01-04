from ConstDefinit import (
    TIME_FRAME,
    column_mapping
) 

def table_header_rename(file_data):
    print(f"[{TIME_FRAME}] table_header_rename(): Start")
    file_data.rename(columns=column_mapping, inplace=True)

def data_cleanUp(file_data):
    print(f"[{TIME_FRAME}] data_clean(): Start")
    file_data = file_data.dropna(axis=0, how='any')
    table_header_rename(file_data)

    # 剔除 pH 值不在 2.9 到 3.9 范围内的数据
    file_data = file_data[(file_data['酸碱度(2.9~3.9)'] >= 2.9) & (file_data['酸碱度(2.9~3.9)'] <= 3.9)]

     # 剔除数据中存在负数的行
    file_data = file_data[(file_data >= 0).all(axis=1)]

    # 剔除质量属性列中数据不在 1~10 区间内的行
    file_data = file_data[(file_data['质量(1~10)'] >= 1) & (file_data['质量(1~10)'] <= 10)]

    # print(f"[{TIME_FRAME}] dataset_preparation(): check first five lines")
    # print(file_data.head())
    return file_data