from typing import Iterator

from loggers import get_logger

logger = get_logger(__name__)


class File:
    """
    Класс для реализации контекст-менеджера File
    Аттрибуты:
        filename - имя файла
        mode - режим для открытия файла
        file_obj - файловый объект, по умолчанию имеет значение None
    """
    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file_obj = None

    def __enter__(self) -> Iterator:
        """ Метод для создания файлового объекта и открытия файла. Если указанного файла не существует, то будет создан
         файл в текущей директории с указанным именем с режимом для записи """
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

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> bool:
        """ Метод для закрытия файла по завершению работы с ним. Любые ошибки которые могут возникнуть при закрытии
        файла игнорируются что позволяет закрыть файл при любых условиях """
        self.file_obj.close()
        logger.info(f"Файл {self.filename} закрыт")
        return True
