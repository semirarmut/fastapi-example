import logging
import sys
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("NO-CONTEXT")

formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s"
)

stream_handler = logging.StreamHandler(sys.stdout)
file_handler = RotatingFileHandler("app.log", backupCount=10, maxBytes=5000000)

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.handlers = [stream_handler, file_handler]

logger.setLevel(logging.INFO)
