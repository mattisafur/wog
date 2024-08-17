"""End to end tests for main_score.py"""

import sys
import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By


def test_scores_service(url: str) -> bool:
    """Tests if score shows up in website and is between 1 and 1000"""
    with selenium.webdriver.Firefox() as driver:
        driver.get(url)

        # raise error if website returns an error
        title = driver.find_element(By.XPATH, "/html/body/h1").text
        if title == "ERROR:":
            raise ValueError

        # get and parse scoreERROR:
        score = driver.find_element(By.ID, "score").text

        parsed_score = int(score)
        if parsed_score is not None:
            if 1 <= parsed_score <= 1000:
                return True
            else:
                return False
        else:
            raise ValueError


def main_function() -> None:
    """Calls test_score_service exists with a return code ased on the result of the function"""
    if test_scores_service("http://127.0.0.1:8777"):
        sys.exit(0)
    else:
        sys.exit(-1)
