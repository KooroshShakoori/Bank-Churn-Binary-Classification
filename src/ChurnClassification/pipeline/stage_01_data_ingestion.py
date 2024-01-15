from ChurnClassification.config.configuration import ConfigurationManager
from ChurnClassification.components.data_ingestion import DataIngestion
from ChurnClassification import logger

STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionTrainPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_file()

if __name__ == '__main__':
    try:
        logger.info(f'Running {STAGE_NAME}...')
        pipeline = DataIngestionTrainPipeline()
        pipeline.main()
        logger.info(f'{STAGE_NAME} completed!...')
    except Exception as e:
        logger.error(f'Error in {STAGE_NAME}! Error: {e}')
        raise e
    