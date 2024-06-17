import sys
import os
import pandas as pd
import numpy as np
from src.utils import load_object
from src.exception import CustomException

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path = os.path.join('artifacts','model.pkl')
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
            print('Before Loading')
            model = load_object(model_path)
            preprocessor = load_object(preprocessor_path)
            print('After Loading')
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
            


class CustomData:
    def __init__(self,
                 Number_of_Customers:int,
                 Menu_Price:float,
                 Marketing_Spend:float,
                 Cuisine_Type:str,
                 Average_Customer_Spending:float,
                 Promotions:str,
                 Reviews:str):
        
        self.Number_of_Customers = Number_of_Customers
        self.Menu_Price = Menu_Price
        self.Marketing_Spend = Marketing_Spend
        self.Cuisine_Type = Cuisine_Type
        self.Average_Customer_Spending = Average_Customer_Spending
        self.Promotions = int(Promotions)
        self.Reviews = Reviews

    
    def get_data_as_dataframe(self):
        try:
            data_input={
                'Number_of_Customers': [self.Number_of_Customers],
                'Menu_Price': [self.Menu_Price],
                'Marketing_Spend': [self.Marketing_Spend],
                'Cuisine_Type': [self.Cuisine_Type],
                'Average_Customer_Spending': [self.Average_Customer_Spending],
                'Promotions': [self.Promotions],
                'Reviews': [self.Reviews]
                }

            data_input_frame = pd.DataFrame(data_input)

            return data_input_frame
        
        except Exception as e:
            raise CustomException(e,sys)

