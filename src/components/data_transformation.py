import os
import sys
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator,TransformerMixin
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from src.utils import save_object

@dataclass
class DataTranformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')


    

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTranformationConfig()

    def get_data_transformation_obj(self):
        try:
            num_col = ['Number_of_Customers', 'Menu_Price', 'Marketing_Spend', 
                       'Average_Customer_Spending', 'Promotions', 'Reviews']
            
            cat_col = ['Cuisine_Type']


            num_pipeline = Pipeline(
                steps = [
                    ("imputer",SimpleImputer(strategy='median')),
                    ("scaler",StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps = [
                    ("imputer",SimpleImputer(strategy='most_frequent')),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )

            logging.info(f'Numerical Preprocessing Complete: {num_col}')
            logging.info(f'Categorical Preprocessing Complete: {cat_col}')

            preprocessor = ColumnTransformer(
                [
                    ("num_pipepline",num_pipeline,num_col),
                    ("cat_pipeline",cat_pipeline,cat_col)
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        

    def initiate_data_transfromation(self,train_path,test_path):
        try:
            logging.info('Entered Data Tranformation Component')

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)


            logging.info('Read Train and Test Data')

            train_df = train_df.drop_duplicates()
            test_df = test_df.drop_duplicates()

            logging.info('Obtaining Preprocessor Object')

            preprocessor_obj = self.get_data_transformation_obj()

            target_col_name = 'Monthly_Revenue'

            input_feature_train_df = train_df.drop(columns=[target_col_name], axis =1)
            target_feature_train_df = train_df[target_col_name]

            input_feature_test_df = test_df.drop(columns=[target_col_name], axis =1)
            target_feature_test_df = test_df[target_col_name]

            logging.info('Applying Preprocessing Object')

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved Preprocessing Object.")

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )


        except Exception as e:
            raise CustomException(sys,e)
