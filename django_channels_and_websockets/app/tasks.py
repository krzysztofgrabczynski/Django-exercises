from celery import shared_task
from celery.utils.log import get_task_logger
from time import sleep


logger = get_task_logger(__name__)


@shared_task
def add(a, b):
    sleep(2)
    result = a + b
    logger.info(f"Result: {result}")
    return result
