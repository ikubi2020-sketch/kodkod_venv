import logging

logging.basicConfig(
    filename="system.log",
    level= logging.INFO,
    format="%(asctime)s, %(levelname)s, %(massage)s"
)

logger = logging.getLogger(__name__)

