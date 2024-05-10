import logging
import time

import schedule

from parser import scrapping

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def job():
    logging.debug("Run scrapping")
    scrapping()


schedule.every().hour.do(job)

job()

while True:
    schedule.run_pending()
    time.sleep(1)
