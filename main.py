from CnnClassifier import logger
from CnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f'>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<')
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<< \n\nx=========x')
except Exception as e:
    raise e
    
STAGE_NAME="PREPARE BASE MODEL"


try:
    logger.info(f"******************************")
    logger.info(f">>>>>>>>>>>>>>stage {STAGE_NAME} started<<<<<<<<<<<<<<<")
    obj=PrepareBaseModelTrainingPipeline()        
    obj.main()
    logger.info(f">>>>>>>>>>>>>stage {STAGE_NAME} completed<<<<<<<<<<<<<<<<<")
except Exception as e:
         
    logger.exception(e)
    raise e
          
         