from cnnClassifier.config import ConfigurationManager
from cnnClassifier.components import PrepareBaseModel
from cnnClassifier import logger


class PrepareBaseModelTrainingPipline:
    def __init(self):
        pass
   
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config=config.get_prepare_base_model_config()
        data_ingestion = PrepareBaseModel(config=data_ingestion_config)
        data_ingestion.get_base_model()
        data_ingestion.update_base_model()