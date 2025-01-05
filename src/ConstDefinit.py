import os
import time



COLUMN_MAPPING = {
    'fixed acidity': '固定酸度(g/L)',
    'volatile acidity': '挥发性酸度(g/L)',
    'citric acid': '柠檬酸(g/L)',
    'residual sugar': '残余糖分(g/L)',
    'chlorides': '氯化物(mg/L)',
    'free sulfur dioxide': '游离二氧化硫浓度(mg/L)',
    'total sulfur dioxide': '总二氧化硫密度(mg/L)',
    'density': '密度(g/ml)',
    'pH': '酸碱度(2.9 - 3.9)',
    'sulphates': '硫酸盐(g/L)',
    'alcohol': '酒精(% vol)',
    'quality': '质量(1 - 10)'
}

FEAT_CHINESE_CHARACTER = [
    '固定酸度(g/L)',
    '挥发性酸度(g/L)',
    '柠檬酸(g/L)',
    '残余糖分(g/L)',
    '氯化物(mg/L)',
    '游离二氧化硫浓度(mg/L)',
    '总二氧化硫密度(mg/L)',
    '密度(g/ml)',
    '酸碱度(2.9 - 3.9)',
    '硫酸盐(g/L)',
    '酒精(% vol)',
    '酸性变量指标总和'
]

ACIDITY_FEAT = {
    'fixed acidity': '固定酸度(g/L)',
    'volatile acidity': '挥发性酸度(g/L)',
    'citric acid': '柠檬酸(g/L)',
    'chlorides': '氯化物(mg/L)',
    'free sulfur dioxide': '游离二氧化硫浓度(mg/L)',
    'total sulfur dioxide': '总二氧化硫密度(mg/L)'
}

COLOR_LIST = ['orange', 'gray', 'green']

# https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009
KAGGLE_DATASET_DOWNLOAD_PATH = "uciml/red-wine-quality-cortez-et-al-2009"
KAGGLE_DATASET_FILE_NAME = "winequality-red.csv"
TIME_FRAME = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
PROJECT_BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DATASET_MINING_RESULT_PATH = os.path.join(PROJECT_BASE_PATH, '..', 'visualizationResult')