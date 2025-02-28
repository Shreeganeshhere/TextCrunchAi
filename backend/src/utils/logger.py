import logging
import os

log_dir = os.path.abspath(os.path.join(os.getcwd(), 'logs'))
os.makedirs(log_dir, exist_ok=True)

Log_file = os.path.join(log_dir, "app.log")

# create logger instance
logger = logging.getLogger("TextcrunchAi")
logger.setLevel(logging.INFO)

# remove any existing handlers
if logger.hasHandlers():
    logger.handlers.clear()

# create file handler
file_handler = logging.FileHandler(Log_file, mode = 'a')
file_handler.setLevel(logging.INFO)

# sets the format of the log messages
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# add the handler to the logger
logger.addHandler(file_handler)

# disable logs from appearing in the console
logger.propagate = False

def setup_logger():
    """returns the logger object

    Returns:
        logger: object of logger to log the messages
    """
    return logger

logger.info("Logger initialized")
setup_logger()