from datetime import datetime

from loggers import get_logger

logger = get_logger(__name__)


class Date:
    """
    Класс для создания объектов, состоящих из соответствующих числовых значений дня, месяца и года.
    Аттрибуты:
        day - день месяца
        month - месяц года
        year - год
    """

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string):
        """
        Метод для форматирования даты из строки в объект класса Date
        Аргументы
            date_string - строковое представление даты
        """
        logger.info("Запущена функция конвертирующая строковое представление даты в объект класса Date")
        if not cls.is_date_valid(date_string):
            return
        my_date = datetime.strptime(date_string, "%d-%m-%Y")
        logger.info("Успешно создан объект класса Date")
        return cls(my_date.day, my_date.month, my_date.year)

    @classmethod
    def is_date_valid(cls, date_string):
        """
        Метод для проверки корректности чисел строкового представления даты
        Аргументы
            date_string - строковое представление даты
        """
        logger.info("Запущена функция проверки корректности введенной даты is_date_valid")
        try:
            datetime.strptime(date_string, "%d-%m-%Y")
            logger.info(f"Указанная дата корректна - {date_string}")
            return True
        except ValueError:
            logger.error(f"Указанная дата не корректна - {date_string}")
            return False

    def __str__(self):
        return f"День: {self.day}, Месяц: {self.month}, Год: {self.year}"
