import sys
from src.components.dataingestion.dataingestion import DataIngestion
from src.exception.exception import ProjectException
import src.logging.logger_setup 

if __name__ == "__main__":
    ingestion = DataIngestion()
    ingestion.initiate_ingestion()