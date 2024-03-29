from CnnClassifier.config.configuration import ConfigurationManager
from CnnClassifier.components.prepare_base_model import PrepareBaseModel
from CnnClassifier import logger


STAGE_NAME="PREPARE BASE MODEL"
class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
            config=ConfigurationManager()
            prepare_base_model_config=config.get_prepare_base_model_config()
            prepare_base_model= PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()


if __name__=="main":
     
    try:
          
          
          logger.info(f"******************************")
          logger.info(f">>>>>>>>>>>>>>stage {STAGE_NAME} started<<<<<<<<<<<<<<<")
          obj=PrepareBaseModelTrainingPipeline()
          obj.main()
          logger.info(f">>>>>>>>>>>>>stage {STAGE_NAME} completed<<<<<<<<<<<<<<<<<")
    except Exception as e:
         logger.exception(e)
         raise e


        