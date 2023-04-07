from data import load,postprocess,preprocess
from model import deepfm


def process(file_path,output_path,drop_column,sparse_column,dense_column,target_column) :

    df = load.load_df(file_path)

    ppc = preprocess.preprocessor(df,drop_column,sparse_column,dense_column,target_column)
    fixlen_feature_columns, feature_names = ppc.embedding()
    linear_feature_columns = fixlen_feature_columns
    dnn_feature_columns = fixlen_feature_columns
    df_1 = ppc.df
    train_x, test_x, train_y = ppc.data_split(feature_names)

    model = deepfm.Deepfm(linear_feature_columns,dnn_feature_columns,train_x,train_y,test_x)
    pred_ans = model.pred()

    postprocess.postprocessor(df,df_1,target_column,pred_ans,output_path)
