import sys, os
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import logging
from src.exception.exception import ProjectException

logger=logging.getLogger(__name__)

@dataclass
class DataIngestionConfig:
    dataset_path:str="dataset/data.csv"

@dataclass
class DataIngestionArtifact:
    raw_data_path:str="artifacts/processed.csv"
    train_data_path:str="artifacts/train.csv"
    test_data_path:str="artifacts/test.csv"

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        self.ingestion_artifact = DataIngestionArtifact()

    def initiate_ingestion(self):
        try:
            logger.info("Starting data ingestion pipeline")
            logger.info("Loading the raw CSV using Pandas")
            df = pd.read_csv(self.ingestion_config.dataset_path)

            logger.info(f"Missing values: \n{df.isnull().sum()}")

            #cleaning
            logger.info("Cleaning dataset")
            logger.info("Resolving missing values and duplicates")
            df=df.dropna()
            df=df.drop_duplicates()
            logger.info("Dataset ready")

            os.makedirs(os.path.dirname(self.ingestion_artifact.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_artifact.raw_data_path, index=False)
            logger.info(f"Saved processed data at{self.ingestion_artifact.raw_data_path}")

            logger.info("Splitting into train and test data")
            train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

            
            logger.info(f"Uploading train data at{self.ingestion_artifact.train_data_path}")
            os.makedirs(os.path.dirname(self.ingestion_artifact.train_data_path), exist_ok=True)
            train_data.to_csv(self.ingestion_artifact.train_data_path, index=False)

            logger.info(f"Uploading test data at{self.ingestion_artifact.test_data_path}")
            os.makedirs(os.path.dirname(self.ingestion_artifact.test_data_path), exist_ok=True)
            test_data.to_csv(self.ingestion_artifact.test_data_path, index=False)
            logger.info("Data Ingestion Completed")

            return(
                self.ingestion_artifact.train_data_path,
                self.ingestion_artifact.test_data_path
            )
        except Exception as e:
            custom_error=ProjectException(e, sys)
            logger.error(custom_error)
            raise custom_error