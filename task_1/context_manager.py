from loggers import get_logger

logger = get_logger(__name__)


class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file_obj = None

    def __enter__(self):
        try:
            self.file_obj = open(self.filename, self.mode)
            logger.info(f"Файл открыт: {self.filename}, режим - {self.mode}")
        except FileNotFoundError:
            self.file_obj = open(self.filename, 'w')
            logger.info(
                f"Указанного файла не существует. В текущей директории был создан и открыт файл: {self.filename}, "
                f"режим - w"
            )
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
        logger.info(f"Файл {self.filename} закрыт")
        return True
