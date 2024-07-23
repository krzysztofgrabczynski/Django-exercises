import requests
import uuid
import os
from celery import shared_task
from celery.utils.log import get_task_logger
from time import sleep
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


logger = get_task_logger(__name__)


def get_filename(url: str) -> str:
    allowed_extensions = ["jpg", "png"]

    try: 
        file_extension = url.split('.')[-1]
        if not file_extension.lower() in allowed_extensions:
            raise ValueError 
    except (ValueError, Exception) as e:
        raise ValueError("Invalid file extension")
    filename = str(uuid.uuid4())
    return f"media/{filename}.{file_extension}" 

@shared_task
def download_image(url: str, client_uuid: str, raise_exception: bool=False):
    try:
        filename = get_filename(url)  
        r = requests.get(url, stream=True)
        
        sleep(7) # long waiting time of the downloading simulation

        with open(filename, "wb") as f:
            for block in r.iter_content(1024):
                if not block:
                    break 
                f.write(block)
    except Exception as e:
        raise_exception = True
        
    if not raise_exception and os.path.getsize(filename) == 0:
            raise_exception = True

    channel_layer = get_channel_layer()
    if raise_exception == True:
        logger.info(f"File saving failed")
        async_to_sync(channel_layer.group_send)(
            client_uuid,
            {
                "type": "send_notification",
                "message": "File saved failed"
            }
        )
    else:
        logger.info(f"File saved succesfully")
        async_to_sync(channel_layer.group_send)(
            client_uuid,
            {
                "type": "send_notification",
                "message": "File saved succesfully"
            }
        )