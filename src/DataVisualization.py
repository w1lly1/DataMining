import os
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


def data_feature_anlysis(file_data):
    print(f"[{TIME_FRAME}] data_anlysis(): Start")

    feature_influence_to_quality_visualize(file_data, "feature_influence_to_quality")

    # multi_feature_analysis(file_data)

    print(f"[{TIME_FRAME}] data_anlysis(): End")
    return file_data


def feature_influence_to_quality_visualize(file_data, file_suffix=""):
    # file_data['酸性变量指标总和'] = file_data['固定酸度(g/L)'] + file_data['挥发性酸度(g/L)'] + file_data['柠檬酸(g/L)']

    sns.set_style('ticks')
    sns.set_context('notebook',font_scale = 1.1)

    plt.figure(figsize = (8, 12))
    for i in range(11):
        plt.subplot(4, 3, i+1)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        sns.boxplot(x = '质量(1 - 10)', y = FEAT_CHINESE_CHARACTER[i], data = file_data, color = COLOR_LIST[i%3], width = 0.6)
        plt.ylabel(FEAT_CHINESE_CHARACTER[i], fontsize = 12)
    plt.tight_layout()

    file_name = f'histograms_{file_suffix}.png'
    output_path = build_output_path(file_name)
    plt.savefig(output_path)


def key_feature_analysis(file_data):
    print(f"[{TIME_FRAME}] key_feature_analysis(): Start")

    key_feature_influence_to_quality_visualize(file_data)

    print(f"[{TIME_FRAME}] key_feature_analysis(): End")


def scatter_plot_visualize(file_data, x_feat, y_feat, file_suffix=""):
    print(f"[{TIME_FRAME}] scatter_plot_visualize(): Start")
    plt.style.use('ggplot')

    plt.figure(figsize = (6,4))
    sns.lmplot(x = x_feat, y = y_feat, hue = '质量(1 - 10)', data = file_data, fit_reg = False, scatter_kws = {'s':10})
    file_name = f'scatter_plot_{file_suffix}.png'
    output_path = build_output_path(file_name)
    plt.savefig(output_path)

def key_feature_influence_to_quality_visualize(file_data):
    print(f"[{TIME_FRAME}] key_feature_influence_to_quality_visualize(): Start")

    # 正负相关参数与质量的散点图
    scatter_plot_visualize(file_data, '固定酸度(g/L)', '柠檬酸(g/L)', "fixed_acidity_and_citric_acid")
    scatter_plot_visualize(file_data, '硫酸盐(g/L)', '挥发性酸度(g/L)', "sulphates_and_volatile_acid")

    # 据图，可知固定酸度在8~12， 柠檬酸浓度在0.3~0.7，挥发性酸度在0.2~0.6，硫酸盐浓度在0.6~1.0之间的红酒质量较好

    print(f"[{TIME_FRAME}] key_feature_influence_to_quality_visualize(): End")
    return file_data


