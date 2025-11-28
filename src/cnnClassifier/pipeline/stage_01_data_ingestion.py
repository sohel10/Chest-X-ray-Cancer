from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger
import os


STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)

        # --- FIX: Skip download if ZIP exists ---
        zip_path = data_ingestion_config.local_data_file

        if os.path.exists(zip_path):
            logger.info(f"Local ZIP found → {zip_path}")
            logger.info("Skipping Google Drive download")
        else:
            logger.info("Local ZIP not found → trying Google Drive download")
            data_ingestion.download_file()

        # --- Extracting ZIP ---
        data_ingestion.extract_zip_file()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e
