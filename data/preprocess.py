import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from deepctr.feature_column import SparseFeat, DenseFeat, get_feature_names


class preprocessor:

    def __init__(self,df,drop_column,sparse_column,dense_column,target_column,split_column = None) :
        self.df = df
        self.drop_column = drop_column
        self.sparse_column = sparse_column
        self.dense_column = dense_column
        self.target_column = target_column
        self.split_column = split_column
        self.preprocess()

    def preprocess(self) :
        print('전처리~')
        self.df = self.df.drop(self.drop_column,axis=1)
        if self.split_column : 
            self.df[self.split_column] = self.df[self.split_column].apply(lambda x :x.split(' ')[0])                                        
        mms = MinMaxScaler()
        self.df[self.dense_column] = mms.fit_transform(self.df[self.dense_column])
        for col in self.sparse_column :
            lbe = LabelEncoder()
            self.df[col] = lbe.fit_transform(self.df[col])
        print('~리처전')


    def data_split(self,feature_names) :
        print('데이터 생성~')
        train_index = self.df[self.target_column].dropna().index.tolist()
        test_index = self.df[self.df[self.target_column].isna()].index.tolist()
        data = self.df[feature_names]
        target = self.df[self.target_column]

        train_x = data.iloc[train_index]
        train_y = target.iloc[train_index]
        test_x = data.iloc[test_index]

        train_model_input = {name: train_x[name] for name in feature_names}
        test_model_input = {name: test_x[name] for name in feature_names}

        # print(len(train_index),len(test_index))
        print('~성생 터이데')
        return train_model_input, test_model_input, train_y

    def embedding(self):
        print('임베딩~')
        fixlen_feature_columns = [SparseFeat(feat, self.df[feat].max() + 1, embedding_dim=4) for feat in self.sparse_column] \
                                + [DenseFeat(feat, 1, ) for feat in self.dense_column]
        dnn_feature_columns = fixlen_feature_columns
        linear_feature_columns = fixlen_feature_columns
        feature_names = get_feature_names(linear_feature_columns+dnn_feature_columns)
        print('~딩베임')
        return fixlen_feature_columns, feature_names
