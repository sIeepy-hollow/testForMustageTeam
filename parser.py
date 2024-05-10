import logging
from datetime import datetime

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from config import Config
from db_utils import read_data_from_db, get_rate
from excel_utils import save_data_to_xlsx
from models import session, ExchangeRate


def scrapping():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('window-size=1920x1080')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(Config.BASE_URL)

    xpath = '/html/body/c-wiz[2]/div/div[4]/div/main/div[2]/div[1]/div[1]/c-wiz/div/div[1]/div/div[1]/div/div[1]/div/span/div/div'

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        rate_text = float(element.text.replace(',', '.'))
        logging.info(f'Exchange rate retrieved: {rate_text}')
    except TimeoutException:
        logging.error(f'Timed out waiting for element with xpath {xpath} to load.')
        return

    current_datetime = datetime.now().replace(minute=0, second=0, microsecond=0)

    if not get_rate(current_datetime):
        new_rate = ExchangeRate(exchange_rate=rate_text, datetime=current_datetime)
        session.add(new_rate)
        session.commit()

    driver.quit()

    df = read_data_from_db()
    save_data_to_xlsx(df)


if __name__ == '__main__':
    scrapping()
