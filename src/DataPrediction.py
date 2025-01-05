from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
from ConstDefinit import (
    TIME_FRAME
)

def dataset_split(file_data):
    labels = file_data['质量(1 - 10)']
    features = file_data.drop('质量(1 - 10)', axis = 1)

    # 对原始数据集进行切分
    train_features,test_features,train_labels,test_labels = train_test_split(features, labels, test_size = 0.3, random_state = 0)

    print('训练特征的规模:', train_features.shape)
    print('训练标签的规模:', train_labels.shape)
    print('测试特征的规模:', test_features.shape)
    print('测试标签的规模:', test_labels.shape)
    return train_features, train_labels, test_features, test_labels

def dataset_split_with_key_features(file_data):
    labels = file_data['质量(1 - 10)']
    features = file_data.drop(columns=['质量(1 - 10)', '残余糖分(g/L)', '氯化物(mg/L)', '游离二氧化硫浓度(mg/L)', '总二氧化硫密度(mg/L)', '密度(g/ml)', '酒精(% vol)'], axis=1)

    # 对原始数据集进行切分
    train_features,test_features,train_labels,test_labels = train_test_split(features, labels, test_size = 0.3, random_state = 0)

    print('训练特征的规模:', train_features.shape)
    print('训练标签的规模:', train_labels.shape)
    print('测试特征的规模:', test_features.shape)
    print('测试标签的规模:', test_labels.shape)
    return train_features, train_labels, test_features, test_labels


def linear_regression_prediction(train_features, train_labels, test_features, test_labels):
    LR = LinearRegression()
    LR.fit(train_features,train_labels)

    prediction = LR.predict(test_features)
    prediction[:5]
    #对模型进行评估
    RMSE = np.sqrt(mean_squared_error(test_labels,prediction))
    print('线性回归模型的预测误差:',RMSE)


def data_prediction(file_data):
    print(f"[{TIME_FRAME}] data_prediction(): Start")
    # print(file_data.dtypes)

    # 线性回归预测
    print('普通线性回归预测')
    train_features,train_labels,test_features,test_labels = dataset_split(file_data)
    linear_regression_prediction(train_features,train_labels,test_features,test_labels)

    # 通过key feature 的线性回归预测
    print('关键特性的线性回归预测')
    train_features,train_labels,test_features,test_labels = dataset_split_with_key_features(file_data)
    linear_regression_prediction(train_features,train_labels,test_features,test_labels)

    return file_data