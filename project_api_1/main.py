import logging

logging.basicConfig(
    level= logging.INFO,
    format="%(asctime)s, %(levelname)s, %(message)s"
)
logger = logging.getLogger(__name__)

file_handler =  logging.FileHandler("system.log", encoding="utf_8")

formatter = logging.Formatter("%(asctime)s, %(levelname)s, %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


