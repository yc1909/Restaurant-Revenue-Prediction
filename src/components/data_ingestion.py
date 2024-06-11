import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTranformationConfig,DataTransformation
from src.components.model_trainer import Model_Trainer,Model_Trainer_Config


@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered The Data Ingestion Component")

        try:
            df = pd.read_csv('notebook\data\Restaurant_revenue.csv')
            logging.info('Read Dataset Into a Dataframe')


            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info('Initiating Train Test Split')

            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Data Ingestion Completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)
        


if __name__ == "__main__":
    data_ingestion_obj = DataIngestion()
    train_data,test_data = data_ingestion_obj.initiate_data_ingestion()

    data_transformation_obj = DataTransformation()
    train_arr,test_arr,_ = data_transformation_obj.initiate_data_transfromation(train_data,test_data)

    model_trainer_obj = Model_Trainer()
    best_score = model_trainer_obj.initiate_model_trainer(train_arr,test_arr)
    print(f'Best score is: {round((best_score * 100),2)}%')




    


