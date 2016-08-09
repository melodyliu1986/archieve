import os
import logging
import logging.config


def logging_simple_config():
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


def logging_config_file(path_config_file):
    logging.config.fileConfig(path_config_file)
    root_logger = logging.getLogger("root")
    root_logger.debug("Root: test!")
    root_logger.info("Info: test!")

    sku_logger = logging.getLogger("skuValidation")
    sku_logger.debug("skuValidation: test!")
    sku_logger.info("skuValidation: test")


if __name__ == "__main__":
    path_config = os.getcwd() + "/logging.conf"
    logging_config_file(path_config)
