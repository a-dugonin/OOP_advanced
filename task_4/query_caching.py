from datetime import datetime
from typing import Any
from loggers import get_logger

logger = get_logger(__name__)


class LRUCache:
    """
    Класс для кеширования ограниченного количества данных запросов
    Аргументы:
        size - размер хеш таблицы
    """

    def __init__(self, size: int) -> None:
        self._size = size
        self._cache = {}
        logger.info(f"Инициализация экземпляра класса LRUCache")

    def get(self, key: Any) -> Any:
        """
        Геттер, для получения элемента по ключу из хеш-таблицы
        Парамеры:
            key - ключ для получения значения
        """
        element = self._cache.pop(key)[0]
        logger.info(f"Получение элемента по ключу {key} из хеш-таблицы. Значение элемента {element}")
        self._cache[key] = [element, datetime.now()]
        logger.info("Обновлен порядок использованных элементов в хеше")
        return element

    @property
    def cache(self) -> Any:
        """ Свойство, позволяющее вернуть самый старый элемент из хеша """
        old_element = min(self._cache.values(), key=lambda x: x[1])[0]
        logger.info(f"Получение самого старого элемента хеш-таблицы. Значение элемента - {old_element}")
        return old_element

    @cache.setter
    def cache(self, new_elem: Any) -> None:
        logger.info("Добавление нового элемента в хеш")
        """
        Сеттер, для добавления элементов в хеш
        Парамеры:
            new_elem - кортеж из ключа и значения, которые необходимо добавить в хеш
        """
        key, value = new_elem
        if len(self._cache) >= self._size:
            logger.info("В хеше максимальное количество элементов. Удаление самого старого элемента из хеша")
            del self._cache[min(self._cache, key=lambda key_dict: self._cache[key_dict][1])]
        self._cache[key] = [value, datetime.now()]
        logger.info("Новый элемент успешно добавлен в хеш")

    def print_cache(self):
        """ Метод для вывода элементов из хеша """
        for key in self._cache:
            print(f'{key}: {self._cache[key][0]}')
        logger.info("Получены все элементы из хеша с использованием метода print_cache")
