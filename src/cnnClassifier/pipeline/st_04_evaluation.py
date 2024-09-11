
from cnnClassifier.config import ConfigurationManager
from cnnClassifier.components import Evaluation
from cnnClassifier import logger


class ModelEvaluationPipline:
    def __init__(self):
        pass
   
    def main(self):
        config = ConfigurationManager()
        validation_config = config.get_validation_config()
        evaluation = Evaluation(config=validation_config)
        evaluation.evaluation()
        evaluation.save_score()