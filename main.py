from loggers import get_logger
from task_1.context_manager import File

logger = get_logger(__name__)

if __name__ == '__main__':
    # Ниже код для запуска скрипта реализованного в рамках task_1
    logger.info("Запуск скрипта из модуля context_manager (task_1)")
    with File('new_file.txt', 'r') as file:
        pass
    logger.info(f"Работа с контекст менеджером завершена")
