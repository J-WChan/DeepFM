import pandas as pd 

def postprocessor(df,df_1,target_column,data,path) :
    print('저장시작')
    index = df_1[df_1[target_column].isna()].index.tolist()
    df.loc[index,target_column] = data
    df.to_csv(path,sep=',')
    print('저장완')