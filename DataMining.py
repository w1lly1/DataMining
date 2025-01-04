import kagglehub
import pandas as pd
import os
import time

TIME_FRAME = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 下载文件
def download_dataset():
    path = kagglehub.dataset_download("abdulmalik1518/the-ultimate-cars-dataset-2024")
    return path

# 主函数
def main():
    print(f"[{TIME_FRAME}] main(): Start")
    dataset_path = download_dataset()
    csv_file_path = os.path.join(dataset_path, "The Ultimate Cars Dataset 2024.csv")

    # 检查文件是否存在
    if not os.path.exists(csv_file_path):
        print(f"[{TIME_FRAME}] main(): File not found at {csv_file_path}")
        return
    else:
        print(f"[{TIME_FRAME}] main(): File found at {csv_file_path}")

    try:
        df = pd.read_csv(csv_file_path, encoding='latin-1')
        print(f"[{TIME_FRAME}] main(): {df.head()}")
    except Exception as e:
        print(f"[{TIME_FRAME}] main(): Error reading CSV file: {e}")


if __name__ == "__main__":
    main()
