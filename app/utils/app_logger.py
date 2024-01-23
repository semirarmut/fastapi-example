import logging
import logging.handlers


class AppLogger:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.__instance = super(AppLogger, cls).__new__(cls)
        return cls.__instance

    def __init__(self, logger_name, file_name) -> None:
        self.logger: logging.Logger = logging.getLogger(name=logger_name)
        self.logger.setLevel(logging.INFO)
        self.__file_name: str = f"{file_name}.log"
        self.setup_logging()

    def setup_logging(self):
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        logging.basicConfig(level=logging.INFO, format=log_format)

        formatter = logging.Formatter(log_format)

        console = logging.StreamHandler()
        console.setFormatter(formatter)

        file = logging.handlers.TimedRotatingFileHandler(filename=self.__file_name, when="midnight", backupCount=7)
        file.setFormatter(formatter)

        self.logger.addHandler(console)
        self.logger.addHandler(file)


app_logger = AppLogger(logger_name="AppLogger", file_name="app").logger
