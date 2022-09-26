from cProfile import label
import sys, os, time, pandas as pd

# model
from sklearn.linear_model import LinearRegression 
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
# selection
from sklearn.model_selection import train_test_split
# metric
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error



# importing ml folder
ml_folder = os.path.dirname(os.path.abspath('../'))
sys.path.insert(0,ml_folder)

from core.delete_unavailable_column import delete_unavailable_column
from core.get_label_type import get_label_type
from core.chunksize_data import chunksize_data
from core.transform_feature_column import transform_feature_column
from core.imputation_feature_column import imputation_feature_column
from core.delete_row_where_label_is_empty import delete_row_where_label_is_empty



class RegressorModel:
    def __init__(self,data_url,data_sep,label):
        # Instantiating a Regressor Model
        self.models = {
            # "xgboost":XGBRegressor(),
            "linear":LinearRegression(),
            "rforest":RandomForestRegressor()
            # "logistic":LogisticRegression()
        }
        self.data_url = data_url
        self.data_sep = data_sep
        self.chuncksize = 1000 
        self.encoding = 'latin-1'
        self.label = label

        self.result_all_model = {} 
        self.result_best_model = {} 

        


    def get_data_(self):
        # chunksize_data
        return chunksize_data(data_url=self.data_url,sep=self.data_sep,chuncksize=self.chuncksize,encoding=self.encoding)
        

    def transform_(self):
        dataframe = self.get_data_()

        # unavailable_column
        dataframe = delete_unavailable_column(dataframe=dataframe)

        # delete_row_where_label_is_empty
        dataframe = delete_row_where_label_is_empty(dataframe=dataframe,label=self.label)
        
        # transform_feature_column
        dataframe = transform_feature_column(dataframe=dataframe,label=self.label) 
        
        # imputation_feature_column
        dataframe = imputation_feature_column(dataframe=dataframe,label=self.label)

        # scaler, normalize, pca 

        return dataframe 
        

    def split_data_(self, shuffle:bool=True, train_size:float=0.3, random_state=42):
        dataframe = self.transform_()
        features = list(set(dataframe.columns) - set([self.label])) # columns without label
        
        X = dataframe[features] 
        y = dataframe[self.label] 

        dataframe = train_test_split(X, y, shuffle=shuffle, train_size=train_size, random_state=random_state)

        return dataframe 


    def evaluate_model_(self, y_test, predictions):
        r2   = r2_score(y_test, predictions)
        rmse = mean_squared_error(y_test, predictions)
        mae  = mean_absolute_error(y_test, predictions)

        result = {"rmse":rmse, "mae":mae, "r2":r2}
        
        return result


    def pipeline(self):
        dataframe = self.split_data_()
        X_train, X_test, y_train, y_test = dataframe 
        
        for model in self.models:
            
            start = time.time()

            ml = self.models[model]
            ml.fit(X_train,y_train) 

            # pred_train = ml.predict(X_train)
            pred_test = ml.predict(X_test)
            
            self.result_all_model[model] = self.evaluate_model_(y_test=y_test,predictions=pred_test)
            
            self.result_all_model[model]['score'] = ml.score(X_test,y_test)

            end = time.time()

            self.result_all_model[model]['time'] = round(float((end-start)/60), 4) 

            time.sleep(2)

        return self.result_all_model 


    def get_best_model(self):
        best_model = {
            "pipeline" : "",
            "score" : 0.0,
            "metrics": {}
        }

        other = []
        models = self.pipeline()

        for model in models:

            other_dict = {}

            other_dict["pipeline"] = str(model)
            other_dict['score'] = float(models[model]['score'])
            other_dict["metrics"] = dict(models[model]) 


            if float(models[model]['score']) >= float(best_model['score']):
                best_model["pipeline"] = str(model)
                best_model['score'] = float(models[model]['score'])
                best_model["metrics"] = dict(models[model])  
            
            other.append(other_dict)

        try:
            other.remove(best_model)
        except:
            pass 

        self.result_best_model = best_model

        return {'best':best_model, 'other':other}


    # def save_best_model(self):
    #     return self.result_best_model 


    # def load_best_model(self):
    #     pass 






