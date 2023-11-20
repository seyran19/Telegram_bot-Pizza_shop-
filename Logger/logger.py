import logging

my_log = logging.getLogger('first_logger')

logging.basicConfig(
    level=logging.INFO,
    filename='tg_bot.log',
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S',
    encoding='utf-8'
)
