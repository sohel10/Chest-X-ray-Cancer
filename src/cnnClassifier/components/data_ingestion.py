import os
import zipfile
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier import logger

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        zip_path = self.config.local_data_file
        if not os.path.exists(zip_path):
            raise FileNotFoundError(f"Local ZIP file not found: {zip_path}")

        logger.info(f"Using local ZIP file: {zip_path}")

    def extract_zip_file(self):
        """
        Extract the zip file.
        """
        zip_path = self.config.local_data_file
        unzip_dir = self.config.unzip_dir

        if not os.path.exists(zip_path):
            raise FileNotFoundError(f"ZIP file missing: {zip_path}")

        os.makedirs(unzip_dir, exist_ok=True)

        logger.info(f"Extracting ZIP: {zip_path}")
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(unzip_dir)

        logger.info(f"Extraction completed → {unzip_dir}")
