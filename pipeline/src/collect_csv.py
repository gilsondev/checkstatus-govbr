import re
from time import sleep
from typing import List, Tuple
from urllib.parse import parse_qs, urlparse

import chromedriver_autoinstaller
from loguru import logger
from pyvirtualdisplay.display import Display
from selenium import webdriver
from selenium.webdriver.common.by import By

DOMAIN_DATASET_PAGE = "https://dados.gov.br/dataset/dominios-gov-br"
RESOLUTION = (1920, 1080)
CHROME_OPTIONS = [
    f"--window-size={','.join(map(str, RESOLUTION))}",
    "--headless",
    "--ignore-certificate-errors",
]


def prepare_display(
    size: Tuple[int, int] = RESOLUTION, visible: bool = False
) -> Display:
    display = Display(visible=visible, size=size)
    display.start()
    return display


def prepare_chrome_driver(options: List[str] = CHROME_OPTIONS) -> webdriver.Chrome:
    chromedriver_autoinstaller.install()

    chrome_options = webdriver.ChromeOptions()
    list(map(lambda arg: chrome_options.add_argument(arg), options))

    return webdriver.Chrome(options=chrome_options)


def fetch_dataset_sheet_link():
    logger.info("Preparing chrome driver...")
    driver = prepare_chrome_driver()

    logger.info("Accessing domain dataset page")
    driver.get(DOMAIN_DATASET_PAGE)

    logger.info("Extract sheet URL")
    dataset_sheet_option = (
        "/html/body/div[3]/div/div[3]/div/article/div/section[2]/ul/li[3]/div/a"
    )
    driver.find_element(By.XPATH, dataset_sheet_option).click()
    sleep(1)

    sheet_link = "/html/body/div[3]/div/div[3]/div/article/div/section[2]/ul/li[3]/div/ul/li[2]/a"
    sheet_link_url = driver.find_element(By.XPATH, sheet_link).get_attribute("href")

    driver.close()

    return sheet_link_url


def prepare_sheet_export_url() -> str:
    raw_url = fetch_dataset_sheet_link()

    query = parse_qs(urlparse(raw_url).query)
    raw_sheet_url = query["url"][0]
    sheet_url = re.sub("/edit.*", "/export?format=csv", raw_sheet_url)

    logger.info("Sheet URL extracted successfully")

    return sheet_url
