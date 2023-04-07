from deepctr.models.deepfm import DeepFM


class Deepfm :

    def __init__(self,linear_feature_columns,dnn_feature_columns,train_model_input,train_y,test_model_input) :
        self.linear_feature_columns = linear_feature_columns
        self.dnn_feature_columns = dnn_feature_columns
        self.train_model_input = train_model_input
        self.train_y = train_y
        self.test_model_input = test_model_input
        self.modeling()
        self.fit()
        
    def modeling(self) : 
        print('모델링')
        self.model = DeepFM(self.linear_feature_columns,self.dnn_feature_columns,task="regression")
        self.model.compile("adam", loss=["mse"],metrics=['mse'])

    def fit(self) :
        print('fit')
        self.model.fit(self.train_model_input, self.train_y,batch_size=256, epochs=100, validation_split=0.2)

    def pred(self) :
        print('pred')
        pred_ans = self.model.predict(self.test_model_input, batch_size=256)
        return pred_ans