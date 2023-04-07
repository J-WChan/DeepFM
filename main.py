import setting
from processor import process_1

if __name__ == '__main__' :
    print('start')
    process_1(setting.file_path,
            setting.output_path,
            setting.drop_column,
            setting.sparse_column,
            setting.dense_column,
            setting.target_column,
            )
    print('end')