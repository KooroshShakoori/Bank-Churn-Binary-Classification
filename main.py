from ChurnClassification import logger
from ChurnClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f'Running {STAGE_NAME}...')
    pipeline = DataIngestionTrainPipeline()
    pipeline.main()
    logger.info(f'{STAGE_NAME} completed!...')
except Exception as e:
    logger.error(f'Error in {STAGE_NAME}! Error: {e}')
    raise e