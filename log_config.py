import os
import logging

error_path = os.getcwd() + "/test2.error"

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

error_logger = logging.getLogger("error logger")
error_logger.setLevel(logging.INFO)

error_handler = logging.FileHandler(error_path)
error_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

error_logger.addHandler(error_handler)
error_logger.addHandler(stream_handler)

error_logger.info("Info: test")
error_logger.error("Error: test")
