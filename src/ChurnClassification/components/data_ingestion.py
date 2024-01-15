import os 
import urllib.request as request
import zipfile
from ChurnClassification import logger
from ChurnClassification.utils.common import get_size
from ChurnClassification.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.sourse_url,
                filename=self.config.local_data_file
            )
            logger.info(f'{filename} is downloading! info: {headers}')

        else:
            logger.info(f'{filename} already exists! with size: {get_size(self.config.local_data_file)}')

    
    def unzip_file(self):
        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_dir)

        logger.info(f'file is unzipped at {self.config.unzip_dir}')