import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from ConstDefinit import (
    TIME_FRAME,
    COLOR_LIST,
    FEAT_CHINESE_CHARACTER,
    DATASET_MINING_RESULT_PATH
) 

# 设置支持中文的字体
mpl.rcParams['font.sans-serif'] = ['SimHei']
# 正确显示负号
mpl.rcParams['axes.unicode_minus'] = False

def build_output_path(file_name="default"):
    # 确保目录存在
    output_directory = DATASET_MINING_RESULT_PATH
    os.makedirs(output_directory, exist_ok=True)

    # 生成文件名
    output_path = os.path.join(output_directory, file_name)

    print(f"[{TIME_FRAME}] dataVisualization(): output_path: {output_path}")
    return output_path


def build_Histograms(file_data, file_suffix=""):
    column = file_data.columns.tolist()
    fig = plt.figure(figsize=(10, 8))
    for i in range(12):
        plt.subplot(4, 3, i + 1)
        file_data[column[i]].hist(bins=100, color=COLOR_LIST[i % 3])
        plt.xlabel(column[i], fontsize=12)
        plt.ylabel('频率', fontsize=12)
    plt.tight_layout()

    file_name = f'histograms_{file_suffix}.png'
    output_path = build_output_path(file_name)
    plt.savefig(output_path)


def build_BoxPlots(file_data, file_suffix=""):
    column = file_data.columns.tolist()
    fig = plt.figure(figsize=(8, 12))
    for i in range(12):
        plt.subplot(4, 3, i + 1)
        sns.boxplot(file_data[column[i]], orient='v', width=0.5, color=COLOR_LIST[i % 3])
        plt.ylabel(column[i], fontsize=12)
    plt.tight_layout()

    file_name = f'boxPlot_{file_suffix}.png'
    output_path = build_output_path(file_name)
    plt.savefig(output_path)


def build_Histograms_and_BoxPlots(file_data, file_suffix=""):
    print(f"[{TIME_FRAME}] dataVisualization(): Start")

    # 绘制直方图
    build_Histograms(file_data, file_suffix)

    # 绘制箱线图
    build_BoxPlots(file_data, file_suffix)
    
    print(f"[{TIME_FRAME}] dataVisualization(): End")


def feature_influence_to_quality_visualize(file_data, file_suffix=""):
    file_data['酸性变量指标总和'] = file_data['固定酸度(g/L)'] + file_data['挥发性酸度(g/L)'] + file_data['柠檬酸(g/L)']

    sns.set_style('ticks')
    sns.set_context('notebook',font_scale = 1.1)

    plt.figure(figsize = (8, 12))
    for i in range(12):
        plt.subplot(4, 3, i+1)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        sns.boxplot(x = '质量(1 - 10)', y = FEAT_CHINESE_CHARACTER[i], data = file_data, color = COLOR_LIST[i%3], width = 0.6)
        plt.ylabel(FEAT_CHINESE_CHARACTER[i], fontsize = 12)
    plt.tight_layout()

    file_name = f'histograms_{file_suffix}.png'
    output_path = build_output_path(file_name)
    plt.savefig(output_path)
