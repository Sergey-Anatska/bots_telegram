# bot/greencard/config.py

import datetime
import os
import logging
logging.basicConfig(level=logging.INFO)

formatter = '[%(asctime)s] %(levelname)8s --- %(message)s (%(filename)s:%(lineno)s)'
logging.basicConfig(
    filename=f'bot-from-{datetime.datetime.now().date()}.log',
    filemode='w',
    format=formatter,
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.WARNING
)


TOKEN = os.environ.get("greencard_info_token")


