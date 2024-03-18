from math import pi

from loggers import get_logger

logger = get_logger(__name__)


class MyMath:
    @classmethod
    def circle_len(cls, radius: int | float) -> float:
        logger.info("Запущена функция вычисления длины окружности circle_len")
        """
        Метод для вычисления длины окружности
        Аргументы
            radius - радиус окружности
        """
        try:
            circle_len = 2 * pi * radius
            logger.info("Функция circle_len отработала корректно")
            return circle_len
        except TypeError:
            logger.error(f"Передано некорректное значение радиуса окружности - {radius}")

    @classmethod
    def circle_sq(cls, radius: int | float) -> float:
        logger.info("Запущена функция вычисления площади окружности circle_sq")
        """
        Метод для вычисления площади окружности
        Аргументы
            radius - радиус окружности
        """
        try:
            circle_sq = pi * radius ** 2
            logger.info("Функция circle_sq отработала корректно")
            return circle_sq
        except TypeError:
            logger.error(f"Передано некорректное значение радиуса окружности - {radius}")

    @classmethod
    def cube_volume(cls, side: int | float) -> int | float:
        logger.info("Запущена функция вычисления объема куба cube_volume")
        """
        Метод для вычисления объема куба
        Аргументы
            side - длина ребра куба
        """
        try:
            cube_volume = side ** 3
            logger.info("Функция cube_volume отработала корректно")
            return cube_volume
        except TypeError:
            logger.error("Значение ребра куба должно быть целым числом или числом с плавающей точкой")

    @classmethod
    def sphere_square(cls, radius: int | float) -> int | float:
        logger.info("Запущена функция вычисления площади поверхности сферы sphere_square")
        """
        Метод для вычисления площади поверхности сферы
        Аргументы
            radius - радиус сферы
        """
        try:
            sphere_square = 4 * pi * radius ** 2
            logger.info("Функция sphere_square отработала корректно")
            return sphere_square
        except TypeError:
            logger.error(f"Передано некорректное значение радиуса сферы - {radius}")
