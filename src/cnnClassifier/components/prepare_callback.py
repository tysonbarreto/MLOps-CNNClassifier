import os
import urllib.request as request
import tensorflow as tf
from pathlib import Path
import time

from cnnClassifier.entity import PrepareCallbacksConfig
from cnnClassifier.config import ConfigurationManager

class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    
    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = self.config.tensorboard_root_log_dir
            
        #     self.config.tensorboard_root_log_dir,
        #     f"tb_logs_at_{timestamp}",
        # )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    

    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=os.path.dirname(self.config.checkpoint_model_filepath),
            save_best_only=True
        )


    def get_tb_ckpt_callbacks(self):
        #print(self.config.tensorboard_root_log_dir,'\n',self.config.checkpoint_model_filepath)
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]
