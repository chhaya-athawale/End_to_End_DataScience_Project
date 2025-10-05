from src.DATA_SCIENCE_PROJECT.pipelines.logger import logging
from src.DATA_SCIENCE_PROJECT.pipelines.exception import CustomException
import sys
from src.DATA_SCIENCE_PROJECT.components.data_ingestion import DataIngestion
from src.DATA_SCIENCE_PROJECT.components.data_ingestion import DataIngestionConfig

if __name__=="__main__":
    logging.info("execution started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custome Exception")
        raise CustomException(e,sys)