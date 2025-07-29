import logging
import os

def get_logger(name):
    os.makedirs("logs", exist_ok=True)  # ✅ Ensure logs directory exists
    logger = logging.getLogger(name)
    handler = logging.FileHandler("logs/test.log")
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] - %(message)s")
    handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(handler)
    return logger
