import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ConstDefinit import (
    TIME_FRAME,
    DATASET_MINING_RESULT_PATH
) 

def data_visualize(file_data):
    print(f"[{TIME_FRAME}] dataVisualization(): Start")
    # 设置调色板
    color = sns.color_palette()
    column= file_data.columns.tolist()
    fig = plt.figure(figsize = (10,8))
    for i in range(12):
        plt.subplot(4,3,i+1)
        file_data[column[i]].hist(bins = 100,color = color[3])
        plt.xlabel(column[i],fontsize = 12)
        plt.ylabel('Frequency',fontsize = 12)
    plt.tight_layout()
    
    # 保存图像为 PNG 文件，并指定保存目录
    output_path = os.path.join(DATASET_MINING_RESULT_PATH, 'histograms.png')
    plt.savefig(output_path)
    
    print(f"[{TIME_FRAME}] dataVisualization(): End")
