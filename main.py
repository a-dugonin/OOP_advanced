from loggers import get_logger
# from task_1.context_manager import File
# from task_2.my_math_module import MyMath
from task_3.date import Date

logger = get_logger(__name__)

if __name__ == '__main__':
    # Ниже код для запуска скрипта реализованного в рамках task_1
    # logger.info("Запуск скрипта из модуля context_manager (task_1)")
    # with File('new_file.txt', 'r') as file:
    #     pass
    # logger.info(f"Работа с контекст менеджером завершена")

    # Ниже код для запуска скрипта реализованного в рамках task_2
    # logger.info("Запуск скрипта из модуля my_math_module (task_2)")
    # res_1 = MyMath.circle_len(radius=5)
    # res_2 = MyMath.circle_sq(radius=6)
    # print(res_1)
    # print(res_2)

    # Ниже код для запуска скрипта реализованного в рамках task_3
    logger.info("Запуск скрипта из модуля date (task_3)")
    date = Date.from_string('10-12-2077')
    print(date)
    print(Date.is_date_valid('10-12-2077'))
    print(Date.is_date_valid('40-12-2077'))
