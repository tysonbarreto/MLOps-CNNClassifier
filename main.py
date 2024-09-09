from cnnClassifier.pipeline import DataIngestionTrainingPipline
from cnnClassifier.pipeline import PrepareBaseModelTrainingPipline
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    data_ingestion = DataIngestionTrainingPipline()
    data_ingestion.main()
    logger.info(f">>> stage {STAGE_NAME} completed \n\nx================x <<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"**************************")
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    prepare_base_model = PrepareBaseModelTrainingPipline()
    prepare_base_model.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e