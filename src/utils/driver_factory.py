import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pathlib import Path

logger = logging.getLogger(__name__)

class DriverFactory:
    @staticmethod
    def create_driver(browser=None, headless=False):
        """
        Factory method to create a WebDriver instance dynamically.
        Supports Chrome and Firefox.
        """
        # Read from parameter first, else from environment
        browser = (browser or os.getenv("BROWSER", "chrome")).lower()
        headless = (
            headless
            or os.getenv("HEADLESS", "false").lower() == "true"
            or os.getenv("CI", "false").lower() == "true"   # 👈 auto headless in CI
        )

        logger.info(f"Creating {browser.capitalize()} driver (headless={headless})")

        if browser == "chrome":
            return DriverFactory._create_chrome_driver(headless)
        elif browser == "firefox":
            return DriverFactory._create_firefox_driver(headless)
        else:
            raise ValueError(f"Unsupported browser: {browser}")

    @staticmethod
    def _create_chrome_driver(headless=False):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        if os.getenv("CI", "false").lower() == "true" or headless:
            options.add_argument("--headless=new")

        # --- FIX: Ensure correct executable path ---
        driver_path = ChromeDriverManager().install()

        # WebDriver Manager sometimes returns the directory instead of the actual binary
        if driver_path.endswith("THIRD_PARTY_NOTICES.chromedriver"):
            fixed_path = driver_path.replace("THIRD_PARTY_NOTICES.chromedriver", "chromedriver")
            if os.path.exists(fixed_path):
                driver_path = fixed_path

        service = ChromeService(driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    @staticmethod
    def _create_firefox_driver(headless=False):
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")

        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver.maximize_window()
        return driver

    @staticmethod
    def take_screenshot(driver, filename):
        """
        Take a screenshot and save it to reports/screenshots.
        """
        try:
            screenshot_dir = Path("reports/screenshots")
            screenshot_dir.mkdir(parents=True, exist_ok=True)
            screenshot_path = screenshot_dir / f"{filename}.png"
            driver.save_screenshot(str(screenshot_path))
            logger.info(f"Screenshot saved: {screenshot_path}")
            return str(screenshot_path)
        except Exception as e:
            logger.error(f"Failed to take screenshot: {str(e)}")
            return None

    @staticmethod
    def quit_driver(driver):
        """Gracefully quit the WebDriver."""
        if driver:
            driver.quit()
